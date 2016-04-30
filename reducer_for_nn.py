#!/usr/bin/env python
import sys

def parsePairs():
    for line in sys.stdin:
        yield (line.strip('\n').split('\t'))

def reducer():
    for key, val in parsePairs():
        line = val.strip('(').strip(')').split(',')
        print '%s 1:%s 2:%s 3:%s 4:%s 5:%s 6:%s 7:%s' % (line[10].strip(' '), line[2].strip(' '), line[3].strip(' '),# line[4].strip(' '),
                                                               line[5].strip(' '), line[6].strip(' '), line[7].strip(' '), line[8].strip(' '), line[9].strip(' '))

if __name__=='__main__':
    reducer()
