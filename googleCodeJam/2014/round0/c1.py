import sys 
import numpy as np 

def myprint(matrix, R, C):
    #  0 mine
    #  1 empty
    for i in range( R ) :
        for j in range( C):
            if i==0 and j==0:
                sys.stdout.write('c')
            elif matrix[i,j] ==0 :
                sys.stdout.write('*')
            else:
                sys.stdout.write('.')
        print 


            

def solve(matrix, R,C, M):
    
    if M == 0 :
        for i in range(R):
            for j in range(C):
                matrix[i,j] =1
        return True

    if M == R * C - 1 :
        return True

    if R == 1 :
        for i in range( R*C - M):
            matrix[0,i] = 1 
        return True
            
    if C == 1 :
        for i in range( R*C - M):
            matrix[i, 0] = 1 
        return True

    if R == 2:
        if M %2 == 1:
            return False
        else:
            for i in range( C - M / 2 ):
                matrix[0,i]=1
                matrix[1,i]=1
            return True
        
    if C == 2:
        if M %2 == 1:
            return False
        else:
            for i in range( R - M / 2 ):
                matrix[i,0]=1
                matrix[i,1]=1
            return True
    
    if R == 4 and C == 4 and M == 3 :
        return False
    
    # case R >= 3 and C >= 3 
    empty = R * C - M 
    if empty <=3 :
        return False

    if empty % 2 ==0 :
        if empty <= 2 * C:
            for i in range(empty /2):
                matrix[0,i]=1
                matrix[1,i]=1
            return True
        else:
            for i in range( empty /C):
                for j in range(C):
                    matrix[i,j] = 1 
            for j in range( empty % C ):
                matrix[ empty/ C , j] = 1
            return True
    else:
        if empty == 5 or empty == 7 :
            return False
        else:
            if  empty <= 2 * C + 1 :
                for i in range( (empty -3) / 2 ):
                    matrix[0,i]=1
                    matrix[1,i]=1
                for i in range(3):
                    matrix[2, i] = 1
                return True
            
            if empty <= 3 * C:
                for i in range( C ):
                    matrix[0,i]=1
                    matrix[1,i]=1
                for i in range(empty - 2 * C):
                    matrix[2,i ]=1
                return True

            else:
                if empty % C == 1:
                    for i in range(  empty /C ):
                        for j in range(C):
                            matrix[i,j] = 1
                    matrix[empty/C ,0:3] =1 
                    matrix[empty/C -1, C-1]=0
                    matrix[empty/C -1, C-2]=0
                    return True

                else:
                    for i in range(  empty /C ):
                        for j in range(C):
                            matrix[i,j] = 1
                    for j  in range( empty % C):
                        matrix[ empty/C, j ] = 1

                    return True
            

    


f = open( sys.argv[1] ) 
N = int( f.readline().strip() ) 

for ncase in range(1, N+1):
    
    print "Case #%d:" % ncase
    
    R, C, M = map( int, f.readline().strip().split() ) 

    matrix = np.zeros((R, C))
    
    if solve(matrix, R, C, M):
        myprint(matrix, R, C) 
    else:
        print "Impossible"




