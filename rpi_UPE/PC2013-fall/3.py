#!/usr/bin/env python 
# this is a template for UPE 

import sys 
#import networkx as nx
import numpy as np 


def solv(maze, row, col ):
    
    helper = np.zeros([row, col] )
    for i in range(col):
        helper[0, i] = maze[0, i]

    for i in range(1, row):
        
        for j in range(col):
            if j>=1 and j <= col-2:
                helper[i, j] = maze[i,j] + min(helper[i-1][j-1], helper[i-1][j] , helper[i-1][j+1]  )
            
            if j == 0 :
                
                helper[i, j] = maze[i,j] + min( helper[i-1][j] , helper[i-1][j+1]  )
            
            if j== col-1:
                helper[i, j] = maze[i,j] + min( helper[i-1][j] , helper[i-1][j-1]  )

    return min( helper[row-1,:] )
                

if __name__ == "__main__":
    f=open(sys.argv[1])
    col = int( f.readline() ) 
    row = int( f.readline() ) 
    
    Maze = np.zeros([row, col])

    for i in range(row):
        
        # print your solution for each test case
        
        tmp = f.readline().split()

        for j in range( len(tmp ) ):
            Maze[i, j ] = tmp[j]

    print "%d" %  solv( Maze, row, col)
            



