import sys

fin = open(sys.argv[1] )

N = int( fin.readline().strip() ) 

for i in range(1,N+1):
    
    row1 = int( fin.readline().strip() ) 
    for j  in range(1,5):
        if j == row1 : 
            arr1 = set(  fin.readline().strip().split() ) 
        else:
            fin.readline()

    row2 = int( fin.readline().strip() ) 
    for j  in range(1,5):
        if j == row2 :
            arr2 = set(  fin.readline().strip().split() ) 
        else:
            fin.readline()

    tmp = arr1 & arr2 
    if len(tmp) == 0 :
        print "Case #%d: Volunteer cheated!" % i
    elif len(tmp) == 1:
        print "Case #%d: %s" %(i, tmp.pop())
    else:
        print "Case #%d: Bad magician!" % i 


