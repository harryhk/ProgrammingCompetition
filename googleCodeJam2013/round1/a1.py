import sys
import pdb

debug = 0

def paint(r, m ):
    return ( 2*r + 2 * m -1 ) * m 

def solve(r,t ):
    # binary search 
    u = 0 
    l = t 
    while u <= l :
        m = (u+l) /2 
        
        if debug:
            if case == 5:
                print u, m, l 

        pm = paint(r, m )
        if pm <t :
            u = m +1  
        if pm > t : 
            l = m -1
        if pm == t :
            return m 
    
    if debug:
        if case == 5 :
            sys.exit(1)

    if paint(r, l) > t :
        return l-1
    else:
        return l
    

fin = open(sys.argv[1])
cases = int( fin.readline() ) 
for case in range(cases):
    
    r, t = map(int, fin.readline().split()  )

    solution = solve(r,t)
    
    #solution = ''
    print "Case #%d: %d" % (case+1, solution) 

