#!/usr/bin/env python 
# this is a template for UPE 

import sys 
#import networkx as nx


def solv(line):
    n = len(line) 
    tmp = -1 
    tline =''
    for i in range(n-1):
        for j in range(i+1, n):
            if isP(line[i:j] ) :
                if tmp < j-i :
                    tmp = j-i
                    #tline = line[i:j]

    return tmp

def isP(l):
    if l == l[::-1]:
        return True
    else:
        return False

        

def solv2(line):
    n = len( line) 

    result = {} 

    for i in range(n -1 ):
        j = i + 1 
        if line[i] == line[j]:
            result[(i, j)] = True 

    for step in range(2, n):
        for i in range( n - step ):
            j = i+ step
            if line[i] == line[ j ]:
                if result.has_key( (i+1, j-1 )) or i+1 == j-1:
                    result[ (i, j) ] = True



   
    return max( [ j-i for i, j in result.keys() ]  ) +1 
         
        
            

if __name__ == "__main__":
    f=open(sys.argv[1])
    #N = int( f.readline() ) 
    
    #for ni in range(N):
        
        # print your solution for each test case
    _ = f.readline() 
    line= f.readline() 
    line = line.strip() 
    print solv2(line)
        


