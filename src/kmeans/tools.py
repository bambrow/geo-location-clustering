#!/usr/bin/env python

# Author: Weiqiang Li
# https://github.com/bambrow/
# lwq088490@gmail.com

import random, math

R = 6371


def closestPoint(point, centers, greatCircle):
    dist = float("+inf")
    closest = 0
    if greatCircle == True:
        for p in centers:
            curDist = GreatCircleDistance(point, p)
            if curDist < dist:
                dist = curDist
                closest = p
    else:
        for p in centers:
            curDist = EuclideanDistance(point, p)
            if curDist < dist:
                dist = curDist
                closest = p
    return centers.index(closest)


def addPoints(c1, c2):
    x1,y1,z1 = c1
    x2,y2,z2 = c2
    return x1+x2, y1+y2, z1+z2


def EuclideanDistance(p1, p2):
    lat1,lon1 = p1
    lat2,lon2 = p2
    x1,y1,z1 = generateCartesian(lat1, lon1)
    x2,y2,z2 = generateCartesian(lat2, lon2)
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return d * R


def GreatCircleDistance(p1, p2):
    lat1,lon1 = p1
    lat2,lon2 = p2
    lat1,lon1,lat2,lon2 = map(math.radians, [lat1,lon1,lat2,lon2])
    dlat = lat2-lat1
    dlon = lon2-lon1
    a = 2*math.asin(math.sqrt((math.sin(dlat/2)**2) + math.cos(lat1)*math.cos(lat2)*(math.sin(dlon/2)**2)))
    return a * R


def generateCartesian(lat, lon):
    lat,lon = map(math.radians, [lat,lon])
    x = math.cos(lat) * math.cos(lon)
    y = math.cos(lat) * math.sin(lon)
    z = math.sin(lat)
    return x,y,z


def generateLatLon(c):
    x,y,z = c
    lat = math.atan2(z,math.hypot(x,y))
    lon = math.atan2(y,x)
    lat,lon = map(math.degrees, [lat,lon])
    return lat,lon


def distance(p1, p2, greatCircle):
    if greatCircle == True:
        return GreatCircleDistance(p1,p2)
    else:
        return EuclideanDistance(p1,p2)



