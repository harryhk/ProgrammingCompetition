import sys
#import pdb
#import numpy as np 
import math
debug = 0


def completeI(i): # i from 0, 1, 2, 3
    return (i+1)*(2* i+1)

def low_bound_i(tot):
    tmp = -3 + math.sqrt( 8 * tot +1 )
    return int( tmp/4.0 ) 

def recheck_low_bound_i(tot, i ):
    assert completeI(i) <= tot
    while completeI(i) <= tot:
        i +=1
    return i-1

def factorial(n):
    if n == 1 or n==0 :
        return 1
    else:
        return reduce( lambda x,y : x*y , [ i for i in range(1, n+1) ] )

def binomal(m , n ):  # m out of n 
    return factorial(n) / factorial(m) / factorial(n - m )
    

def binmolSum(y, remain):
    return sum([  binomal(i, remain)   for i in range(y, remain+1) ] ) * ( 0.5 ** remain ) 
    

def tricky(remain, ybase, x, y):
    remain = remain - 2 * ybase
    y += 1 # how many of y  fail 
    y = y - ybase
    # at least y of remain fall in on side 
    if y > remain :
        return 0.0
    else:
        return binmolSum(y, remain)


fin = open(sys.argv[1])
#fout = open(sys.argv[1]+'.out', 'w')
cases = int( fin.readline() ) 

for case in range(cases):
    
    tot , x, y = map( int, fin.readline().split() ) 
    x = abs(x) 
    
    i = low_bound_i(tot)
    i = recheck_low_bound_i(tot, i )

    remain = tot - completeI(i)
    ybase = 0  # upper bond for y 
    if remain  > 2 * i + 2 :
        ybase = remain - ( 2 * i + 2 )
        

    if x + y <= 2 *i :
        solution = 1.0
    elif x+ y >= 2 * i + 4 :
        solution = 0.0 
    elif y < ybase:
        solution = 1.0
    else:
        solution = tricky( remain, ybase, x, y )

    print >> sys.stdout, "Case #%d: %g" % (case+1, solution) 
    sys.stdout.flush()


