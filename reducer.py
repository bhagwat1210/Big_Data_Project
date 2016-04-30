#!/usr/bin/env python
import sys

def parsePairs():
    for line in sys.stdin:
        yield (line.strip('\n').split('\t'))

def reducer():
    for key, val in parsePairs():
        line = val.strip('(').strip(')').split(',')
        print '%s 1:%s 2:%s 3:%s 4:%s 5:%s 6:%s 7:%s 8:%s' % (line[10], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])

if __name__=='__main__':
    reducer()
