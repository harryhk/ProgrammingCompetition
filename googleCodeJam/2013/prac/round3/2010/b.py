import sys
#import pdb
#import numpy as np 
import math
debug = 0

def solve(n):
    lower = 0
    upper = n
    count = 0
    while lower != upper -1 :
        lower = int( ( lower + upper ) /2.0 )  
        count +=1 

    return count

fin = open(sys.argv[1])
#fout = open(sys.argv[1]+'.out', 'w')
cases = int( fin.readline() ) 

for case in range(cases):
    l, p , c = map( float, fin.readline().split() ) 
    n = math.ceil( math.log(p/l) / math.log(c)  )
    n = int(n) 
    solution = solve(n)
    print >> sys.stdout , "Case #%d: %d" % (case+1, solution) 



