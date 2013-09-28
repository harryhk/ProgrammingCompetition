import sys
import pdb
#import numpy as np 

debug = 0


class Game(object):
    def __init__(self, E, R, N, line):
        self.e, self.r , self.n = E, R, N 
        # ( value, index ) 
        self.v =   map( int, line.split() )  
        self.nv = len(self.v)

        #self.argsort = np.argsort(self.v)
        #self.argsort = self.argsort[::-1]
        tmp = [ (j, i) for i, j in enumerate(self.v)  ]
        tmp.sort(reverse = True)
        self.argsort = [ i[1] for i in tmp  ]

        self.upper = [ self.e for _ in range(self.nv) ]
        self.lower = [ 0      for _ in range(self.nv) ]
        self.spend = [ 0      for _ in range(self.nv) ]
        self.status= [ 0      for _ in range(self.nv) ]

        if debug:
            pdb.set_trace()
    
    
    def set_bound(self, idx):
        for i in range(idx+1, self.nv ):
            if self.status[i] == 0:
                self.upper[i] = min( self.lower[idx] + (i-idx) * self.r, self.e ) 
            else:
                break
        for i in range(idx-1, -1, -1):
            if self.status[i] == 0:
                self.lower[i] = max( 0, self.upper[idx] -  (idx-i)* self.r )
            else:
                break


    def solve(self):
        # global constraint  
        if self.e <= self.r:
            return sum([ i for i in  self.v] ) * self.e

        for idx in self.argsort:
            self.spend[idx] = self.upper[idx] - self.lower[idx]
            self.status[idx] = 1 
            self.set_bound(idx)

        
       
        if debug:
            pdb.set_trace()

        return sum( [ i* j for i, j in zip( self.v, self.spend ) ] )
        

fin = open(sys.argv[1])
cases = int( fin.readline() ) 
for case in range(cases):
    e, r, n = map(int,  fin.readline().split() )
    line = fin.readline().strip()
    game = Game(e, r, n, line)
    
    solution = game.solve()

    print "Case #%d: %d" % (case+1, solution) 



