#!/usr/bin/env python 
# this is a template for UPE 

import sys 
import networkx as nx
 


def solv(word, T ):
    
    vlist = T.successors('0')
    nw = len(word) 
    
    c=1
    tmp = ''
    while vlist and c <= nw:
        
        if word[:c] in vlist:
            vlist = T.successors( word[:c] )
            tmp += word[:c]
            c+=1
        else:
            # left most leave 
            s = sorted( vlist )[0]
            tmp += s 
            tmpS = T.successors( s )

            while tmpS :
                s = sorted(tmpS)[0]
                tmp += s
                tmpS = T.successors(s)
            
    return tmp
        




if __name__ == "__main__":
    f=open(sys.argv[1])
    N = int( f.readline() ) 
    
    # build trie
    T = nx.DiGraph() 
    
    # use hash map store all prefix
    for i in range(N):
        tmp=  f.readline().strip()
        T.add_edge('0',  tmp[0]  )
        for j in range(1, len( tmp) ) :
                T.add_edge(tmp[:j], tmp[:j+1])


    print T.__dict__

    N = int( f.readline() )
    
    lQ = []

    for i in range(N):
        lQ.append( f.readline().strip() )  


    for i in lQ:
        print   solv( i, T )
