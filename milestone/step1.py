# Author: Weiqiang Li
# https://github.com/bambrow/
# lwq088490@gmail.com

import sys
from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print >> sys.stderr, "Usage: step1.py <input> <output>"
        exit(-1)

    sc = SparkContext()

    sc.textFile(sys.argv[1]) \
      .map(lambda line: line.split(line[19])) \
      .filter(lambda fields: len(fields) == 14) \
      .map(lambda fields: [fields[12], fields[13], fields[0], fields[1], fields[2]]) \
      .filter(lambda fields: fields[0] != "0" and fields[1] != "0") \
      .map(lambda fields: [fields[0], fields[1], fields[2], fields[3].split()[0], fields[3].split()[1], fields[4]]) \
      .map(lambda fields: ",".join(fields)) \
      .saveAsTextFile(sys.argv[2])


    sc.stop()

