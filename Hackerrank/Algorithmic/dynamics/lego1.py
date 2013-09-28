import numpy as np 
lego=[1,2,3,4]

def solv(row, col):
    #r=[0] * ( col+1 ) 
    r = np.zeros(col+1)
    r[0]=1
    for ri in range(1, col+1):
        for legolen in lego:
            if ri - legolen >=0:
                r[ri] += r[ri- legolen]
    #for ri in range(1, col+1):
    #   r[ri] = r[ri]**row
    
    r **= row

    #c = [ [ 0 for x in range(col+1)]  for y in range(col+1) ] 
    c = np.zeros((col+1, col+1))
    c[1,1]= 1

    for cj in range(2, col+1):
        s=0
        for cn in range(2, cj):
            for i in range(1, cj):
                c[cn,cj]+= c[cn-1,i]* c[1,cj-i]
            s += c[cn,cj]
        c[cj,cj]=1
        s+=1
        c[1,cj] = r[cj]  -s
        
        #for nn in range(2, cj+1):
         #   c[1,cj] -= c[nn,cj]

    return int( c[1,col] % 1000000007);





n = int( raw_input() ) 
for i in range(n):
    (row, col) = raw_input().split()
    row = int(row)
    col = int(col)
    print solv(row, col)
