import sys
#import pdb
#import numpy as np 
#import math
debug = 0


def cross(wire_a, wire_b):
    if ( wire_a[0] - wire_b[0] ) * (wire_a[1]- wire_b[1]) < 0 : 
        return True
    else:
        return False

fin = open(sys.argv[1])
#fout = open(sys.argv[1]+'.out', 'w')
cases = int( fin.readline() ) 

for case in range(cases):
    n = int( fin.readline() ) 
    wires = []
    for i in range(n):
        tmp = map( int , fin.readline().split() )
        wires.append(tuple(tmp) ) 
    count = 0
    for i in range(n-1):
        for j in range(i+1, n ):
            if cross( wires[i], wires[j] ):
                count +=1 

    solution = count 
    print >> sys.stdout , "Case #%d: %d" % (case+1, solution) 



