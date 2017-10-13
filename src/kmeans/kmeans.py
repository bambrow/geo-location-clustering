#!/usr/bin/env python

# Author: Weiqiang Li
# https://github.com/bambrow/
# lwq088490@gmail.com

import sys, random, math, logging
from pyspark import SparkContext
from tools import *


def parse(argv):

    # check if the command line arguments are valid
    if len(argv) != 5 or (argv[4] != 'Euclidean' and argv[4] != 'GreatCircle'):
        print >> sys.stderr, 'Usage: {0} <input> <output> <k> <Euclidean|GreatCircle>'.format(argv[0])
        sys.exit(-1)
    
    k = 0

    # parse k and check if k is valid
    try:
        k = int(argv[3])
        assert k > 0, 'k is equal or smaller than 0!'
    except AssertionError as e:
        print >> sys.stderr, 'k must be greater than 0!'
        logging.exception(e)
        sys.exit(1)
    except ValueError as e:
        print >> sys.stderr, 'k must be an integer!'
        logging.exception(e)
        sys.exit(1)
    return k


def kmeans(parsed, k, argv):

    # generate the rdd of (lat,lon) coordinates and (x,y,z) coordinates; persist this rdd
    cartesian = parsed.map(lambda (lat,lon): ((lat,lon), generateCartesian(lat, lon))).persist()

    # stop iteration if the mean distance change of centers <= 0.1
    convergeDist = 0.1 
    # the mean distance change of centers
    tempDist = float("+inf") 
    # determine which distance measure method should be used
    greatCircle = True if argv[4] == 'GreatCircle' else False
    # randomly choose samples from all points; pre-set the seed in order to compare between methods 
    currentCenters = parsed.takeSample(False, k, 1) 

    # iteration
    while tempDist > convergeDist:

        # find closest center for each point; use (x,y,z) coordinates for average calculation
        assigned = cartesian.map(lambda (p,cart): (closestPoint(p, currentCenters, greatCircle), cart))
        # group and sum all the points accoring to the center
        grouped = assigned.reduceByKey(lambda c1,c2: addPoints(c1,c2)).sortByKey()
        # calculate the new centers
        newCenters = grouped.map(lambda (i,c): (i, generateLatLon(c))).collect()

        # calculate the average distance change between old centers and new centers
        tempDist = reduce(lambda x,y: x+y, 
                          map(lambda p1,p2: distance(p1,p2,greatCircle), 
                              currentCenters, [x[1] for x in newCenters])) / float(len(newCenters))

        # print information on the screen
        print "#" * 80
        print "Old Centers:", currentCenters
        print "New Centers:", [x[1] for x in newCenters]
        print "Average Distance Change:", tempDist
        print "#" * 80

        for i,p in newCenters:
            currentCenters[i] = p

    # print the final centers
    print "#" * 80
    print "Final Centers:", currentCenters
    print "#" * 80

    # put the final centers into rdd, with id -1 in order to draw them (the actual center id starts with 0)
    finalCenters = grouped.map(lambda (i,c): (i, generateLatLon(c))) \
      .map(lambda (i,p): (p, -1))
    # get the final assignments and union with the center
    finalAssigned = cartesian.map(lambda (p,cart): (p, closestPoint(p, currentCenters, greatCircle))) \
      .union(finalCenters) \
      .map(lambda ((lat,lon),i): str(lat) + "," + str(lon) + "," + str(i))
    finalAssigned.saveAsTextFile(argv[2])


