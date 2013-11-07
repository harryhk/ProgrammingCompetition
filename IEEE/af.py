#!/usr/bin/env python 

import sys

L=range(1, 1337+1)


def solv(pos):
    
    c = 1 
    ptr = 0
    direction = 0 # 0 right, 1 left 
    while c < pos:
        c = c+1
        
        if direction == 0:
            ptr = (ptr+1) % 1337
            if c % 7 ==0 or str(c).find('7') != -1 :
                direction =1 - direction 

        else: 
            ptr = (ptr -1) % 1337 
            if c % 7 ==0 or str(c).find('7') != -1 :
                direction =1 - direction 




    print L[ptr] 

        



if __name__ == "__main__":
    
    n = sys.stdin.readline()
    n = int( n.strip() ) 

    for _ in range(n) :
        
        pos = int( sys.stdin.readline().strip() )

        solv(pos) 
