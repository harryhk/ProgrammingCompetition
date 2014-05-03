import sys 
import numpy as np


def solve(grass, grass_raw,  n, m):
    for i in range(n):
        row = grass[i,:]
        m_row = max(row)
        #if m_row == row[0] or m_row == row[-1]:
        for j in range(m):
            grass_raw[i,j] = m_row if grass_raw[i,j] >= m_row else grass_raw[i,j]

    for j in range(m):
        col = grass[:,j]
        m_col = max(col)
        #if m_col == col[0] or m_col == col[-1]:
        for i in range(n):
            grass_raw[i,j]= m_col if grass_raw[i,j] >= m_col else grass_raw[i,j]

    
    for i in range(n):
        for j in range(m):
            if grass_raw[i,j] != grass[i,j]:
                return "NO"
    
    return "YES"
    

            

    

f = open(sys.argv[1])
N = int(f.readline())

for i in range(N):
    n, m = f.readline().split()
    n, m = ( int(n), int(m)  )

    grass = []
    for _ in range(n):
        grass.append( f.readline().strip().split() )

    grass = np.array(grass, dtype= int)
    grass_raw = np.ones_like(grass) * 100
    
    #print game
    print "Case #%d: %s" %( i+1, solve(grass, grass_raw,  n, m) )  
