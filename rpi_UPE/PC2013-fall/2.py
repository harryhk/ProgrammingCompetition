#!/usr/bin/env python 
# this is a template for UPE 

import sys 
#import networkx as nx
 


_debug = 0


def solv( word , lI):
    
    
    n = len(word)
    for i in range(1,n+1)[::-1]:
        if lI.has_key(word[:i] ):
            return sorted(lI[ word[:i]  ])[0]

    return None 



if __name__ == "__main__":
    f=open(sys.argv[1])
    N = int( f.readline() ) 
    
    lI = {}
    noreturn = []
    # use hash map store all prefix
    for i in range(N):
        tmp=  f.readline().strip()
        noreturn.append(tmp)
        for j in range( 1, len(tmp)  ):
            tmpW = tmp[:j]
            if lI.has_key(tmpW ):
                lI[ tmpW ].append( tmp )
            else:
                lI[ tmpW] = [ tmp ]



    if _debug:
        print lI

    N = int( f.readline() )
    
    lQ = []

    for i in range(N):
        lQ.append( f.readline().strip() )  


    for i in lQ:
        tmp =  solv( i, lI )
        if tmp:
            print tmp
        else:
            print sorted(noreturn)[0]
