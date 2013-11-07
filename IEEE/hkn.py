#!/usr/bin/env python 

import sys

_debug = 0

def num2BinStr(a):
    # change int to binary string

    return bin(a)[2:]

def isPalin(binStr):
    return binStr == binStr[::-1]

def binStr2Int(s):
    return int( s, 2)

def nextPalin(a):
    # find next palindrom after a 
    abinS = num2BinStr(a)
    length = len(abinS)

    oddDig = ( length %2 == 1)
    middle = abinS[ (length -1) /2   ]
    leftHalf = abinS[:length/2]
    
    if oddDig:
        increment = pow(2, length/2)
        newNum = int( leftHalf + middle + leftHalf[::-1]  ,2)
    else:
        increment = pow(2, length/2) + pow(2, length/2-1)
        newNum = int( leftHalf + leftHalf[::-1] ,2 ) 

    if newNum > a:
        return newNum

    if middle != '1':
        return newNum + increment
    else:
        inc = pow(2, (length/2) +1 ) 
        numRoundUp = ( a / inc +1 )  * inc
        return nextPalin( numRoundUp )



def solv(a,b):
    
    abin = num2BinStr(a) 

    c=0
    if isPalin(abin):
        c+=1
        a = a+1

    anext = nextPalin(a)


    while anext <= b:
        
        if _debug:
            print anext, num2BinStr(anext) 

        c = c+1
        anext = anext +1 
        anext = nextPalin(anext)

    return c





if __name__ == "__main__":
   
    line = sys.stdin.readline()

    while line:
        
        a, b = [ int(i) for i in line.strip().split(',')  ]

        print solv(a,b)
        line = sys.stdin.readline()


    

