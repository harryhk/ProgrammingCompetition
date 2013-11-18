#!/usr/bin/env python 
# this is a template for UPE 

import sys 
import numpy as np
#import networkx as nx

_debug = 0

def solv(s1, originSeq):
    

    for i in range( len( originSeq )) :
        if i== 0:
            tmp = originSeq[i]
            tmpmin = emin(s1, originSeq[i] )
        else:
            
            tmpmin2 = emin(s1, originSeq[i])
            if tmpmin > tmpmin2:
                tmp = originSeq[i]
                tmpmin = tmpmin2

    return tmp 

def emin(l1, l2):
    
    n1 = len(l1) +1 
    n2 = len(l2) +1 

    if _debug:
        print l1, l2

    T = np.zeros( [n1, n2]  )
    
    for i in range(n1):
        T[i, 0] = i

    for i in range(n2):
        T[0, i] = i

    if _debug:
        print T

    for i in range(1, n1):
        for j in range(1, n2):
            tmp = [ 1+T[i-1, j] , 1+ T[i, j-1], mydiff(l1[i-1], l2[j-1]) + T[i-1, j-1]   ]
            T[i,j] = min(tmp) 

    return T[n1-1, n2-1]
                

def mydiff( i, j ):
    if i==j :
        return 0 
    else:
        return 1

if __name__ == "__main__":
    f=open(sys.argv[1])
    oN = int( f.readline() ) 

    
    originSeq = []
    for _ in range( oN  ):
        
        originSeq.append( f.readline().strip()  )
    
    uN = int( f.readline() )

    unknownSeq = []

    for _ in range(uN):
        unknownSeq.append( f.readline().strip()  )

    if _debug:
        print originSeq
        print unknownSeq

    for l in unknownSeq :
        print solv( l, originSeq  )
    


