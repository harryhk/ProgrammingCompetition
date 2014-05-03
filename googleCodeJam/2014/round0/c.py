import sys 
import numpy as np 

def printMap(nMap):
    
    for i in size(nMap, 0) :
        for j in size(nMap, 1):
            if nMap[i,j] == 0:
                sys.write('*')
            elif nMap[i,j] == 1:
                sys.write('c')
            else:
                sys.write('.')
        sys.write('\n')
    sys.write('\n')

def test( mMap, start, M, size):
    if M == size -1:
        printMap(nMap)
        return True
        
    
    


fin = open( sys.argv[1] ) 

N = int( fin.readline().split() ) 

for n in range( 1, N+1):
    
    R, C, M= map( int, fin.readline().split() ) 

    mMap = np.zeros((R,C))

    Rend = (R+1)/2 
    Cend = (C+1)/2
    
    print "Case #%d:" % n
    poss = False
    for ir in range( Rend):
        for ic in range( Cend) :
            start = ( ir, ic) 
            mMap[ir, ic] = 1
            poss= test( mMap, start, M , R*C):
            if poss:
                break
            else:
                mMap[ir, ic] = 0 

        if poss:
            break 

    if not  poss:
        print "Impossible"


                
                
                




