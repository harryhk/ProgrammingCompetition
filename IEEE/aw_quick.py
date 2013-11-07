#!/usr/bin/env python 


import sys

from string import maketrans
import itertools

_debug = 1

class Prob(object):
    def __init__(self, n ) :
        self.dictionaryChars = set()
        self.dct=set()

        for i in range(n):
            item = sys.stdin.readline().strip()
            self.dct.add(item)
            for j in item:
                self.dictionaryChars.add(j)

        tmp = sys.stdin.readline()

        self.encryOrig = sys.stdin.readline().strip().lower()

        self.encryChars =set()

        self.encry = self.encryOrig.split()

        for i in self.encry:
            for j in i:
                self.encryChars.add(j)


    
    def solv(self):
        # brutal force 

        
        score = -1 
        encry = [ i for i in self.encryChars  ]
        bestTab = None
        for i in itertools.permutations( self.dictionaryChars, len(self.dictionaryChars)  ):
            
            if _debug:
                print ''.join( encry ), ''.join(i)

            tmpTab = maketrans(''.join( encry ), ''.join(i) )
            c=0

        

            for encryItem in self.encry:
                encryItem.translate(tmpTab)

                if _debug:
                    print encryItem

                if encryItem  in self.dct:
                    c = c+1
            if c > score:
                score = c 
                bestTab = tmpTab

        print score ,  self.encryOrig.translate( bestTab ).upper()


    def p(self):
        print self.__dict__


if __name__ == "__main__":

    line =  sys.stdin.readline()
    
    while line:
        
        n = int( line.strip() )
        prob = Prob(n)
        
        if _debug:
            prob.p()
        
        #prob.solv()

        line = sys.stdin.readline()
    

