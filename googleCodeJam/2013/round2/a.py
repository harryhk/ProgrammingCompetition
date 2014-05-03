import sys
import pdb
#import numpy as np 
#import math
debug = 0



fin = open(sys.argv[1])
fout = open(sys.argv[1]+'.out', 'w')
cases = int( fin.readline() ) 

for case in range(cases):
    
    a , n = map(int , fin.readline().split() ) 
    motes = map( int, fin.readline().split() ) 
    

    if debug:
        if case == 89:
            pdb.set_trace()
    motes.sort()
    current = a
    oper   = 0 
    
    optim={} # store current value : oper
    optim[a] = 0 

    for motes_idx in range(len( motes) ):
        mote_i = motes[motes_idx]
        optim_c = {}
        for current in optim:
            if mote_i < current:
                if optim_c.has_key(current + mote_i):
                    optim_c[current+ mote_i] = min( optim_c[current + mote_i]  ,optim[current] )
                else:
                    optim_c[current+ mote_i] = optim[current] 
                    
            else:
                # add 
                oper = 0 
                new_current = current
                if new_current != 1:
                    while new_current <= mote_i:
                        new_current += new_current -1
                        
                        oper += 1
                    if optim_c.has_key(new_current + mote_i):
                        optim_c[new_current+ mote_i] = min( optim_c[new_current + mote_i],  optim[current] + oper )
                    else:
                        optim_c[new_current+ mote_i] = optim[current] + oper
                        
                # delete
                if optim_c.has_key(current):
                    optim_c[current] = min( optim_c[current], optim[current] +1 )
                else:
                    optim_c[current] = optim[current] +1
        optim = optim_c
    
    sol = optim.values()
    sol.sort()
    solution = sol[0]
    print >> fout , "Case #%d: %d" % (case+1, solution) 



