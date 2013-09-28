import sys
import pdb

debug =0 

fin = open(sys.argv[1])
cases = int( fin.readline() ) 

for case in range(cases):
    if debug:
        pdb.set_trace()
    n,k,b,t = map( int , fin.readline().split() ) 
    xi = map( int, fin.readline().split() ) 
    vi = map( float, fin.readline().split() ) 
    arrive_time = [ ( b - xi[i] ) / vi[i]  for i in range(n) ]
    if len( [i for i in arrive_time if i <= t] ) < k :
        solution = 'IMPOSSIBLE'
    else:
        count = 0
        swap = 0
        for i in range( n-1, -1 , -1  ):
            if count == k:
                break
            if arrive_time[i] <= t :
                count += 1
            else:
                swap += k - count 
        
        solution = str(swap) 
    
    print "Case #%d: %s" % (case +1, solution)



