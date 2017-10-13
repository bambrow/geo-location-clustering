#!/usr/bin/env python

# Author: Weiqiang Li
# https://github.com/bambrow/
# lwq088490@gmail.com

import sys
from pyspark import SparkContext
from kmeans.kmeans import *


if __name__ == '__main__':

    # see if the command line inputs are valid and parse k
    k = parse(sys.argv)

    sc = SparkContext()

    # parse data into (lat,lon) pairs
    data = sc.textFile(sys.argv[1])
    parsed = data.map(lambda line: line.split()) \
      .filter(lambda fields: len(fields) == 3 and fields[0] != 'Latitude') \
      .map(lambda fields: (float(fields[0]),float(fields[1])))
    
    # run kmeans (see kmeans folder)
    kmeans(parsed, k, sys.argv)
        

    sc.stop()



