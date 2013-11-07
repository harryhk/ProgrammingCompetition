#!/usr/bin/env python 

import sys

_debug = 1


class Problem(object):

    def __init__(self, line1, line2):
        
        tmp= [ int(i) for i in line1.strip().split(' ')]
        self.nshows = tmp[0] 
        self.shows = [ i for i in tmp[1:]  ]

        tmp = [ int(i) for i in line2.strip().split(' ')]
        self.nkeys = tmp[0] 
        self.keys= zip( tmp[1::2],  tmp[2::2] )
        # sort keys accord to priority

        self.keys.sort(key= lambda x: x[1] )

    
    def solv(self):

        for keyEvt, _ in self.keys :
            
            
        pass

    def p(self):
        print self.__dict__

if __name__ == '__main__':
    
    line1 = sys.stdin.readline()

    while line1:
        
        line2 = sys.stdin.readline()

        prob = Problem(line1, line2)

        if _debug:
            prob.p()

        prob.solv()

        line1 = sys.stdin.readline()
