import sys 
import numpy as np 

def palid(num):
    num_s = str(num)
    return num_s == num_s[::-1]


def solve( n, m):
    count = 0
    n_s = int( np.sqrt(n) ) if np.sqrt(n) == int(np.sqrt(n)) else int(np.sqrt(n))  +1
    m_s = int( np.sqrt(m) ) 
    for i in range(n_s, m_s+1 ):
        if palid(i):
            ii = i * i 
            #if ii >= n and ii <= m and palid(ii) :
            if palid(ii) :
                print i , ii
                count += 1

    return count
    
    

            

    

f = open(sys.argv[1])
N = int(f.readline())

for i in range(N):
    n, m = f.readline().split()
    n, m = ( int(n), int(m)  )

    
    print "Case #%d: %s" %( i+1, solve(n, m) )  
    break
