import sys
import pdb
#import numpy as np 

debug = 0


class Game(object):
    def __init__(self, E, R, N, line):
        self.e, self.r , self.n = E, R, N 
        self.v = map( int, line.split() )
        self.nv = len(self.v)
        self.max_left = self.e -self.r
        self.gain_pre = [ ( self.e - left ) * self.v[0] for left in range(self.max_left +1 ) ]

        self.spent_trace = [ [] for _ in range(self.nv)  ]
        for i in range(self.nv):
            self.spent_trace[i] = [ -1 for _ in range(self.max_left + 1) ]


    def solve(self):
        
        #if debug:
        #    if case == 89:
        #        pdb.set_trace()

        if self.max_left <=0:
            return sum(self.v) * self.e 

        for vi in range(1, self.nv):
            self.gain = [ 0 for _ in range(self.max_left +1 ) ]
            for x in range(self.max_left +1):
                tmp_max = -1
                y_start = x - self.r 
                if y_start < 0:
                    y_start = 0

                for y in range( y_start, self.max_left+1 ):
                    tmp = self.gain_pre[y] + ( y + self.r - x) * self.v[vi] 
                    if tmp_max < tmp:
                        tmp_max = tmp
                        self.spent_trace[vi][x] = y
                self.gain[x] = tmp_max
        
            self.gain_pre = self.gain

        if debug:
            print self.spent_trace

        return max(self.gain_pre)
    
    def vi_left(self):
        if self.max_left <= 0:
            return repr( [ 0 for _ in range(self.nv) ]  )
        
        left = []
        tmp_idx = self.gain_pre.index( max(self.gain_pre) )
        left.append(  tmp_idx )
        for i in range( self.nv -1 , 0, -1 ):
            tmp_idx_pre = self.spent_trace[i][tmp_idx]
            left.insert(0, tmp_idx_pre  )
            tmp_idx = tmp_idx_pre

        return left


fin = open(sys.argv[1])
cases = int( fin.readline() ) 
for case in range(cases):
    e, r, n = map(int,  fin.readline().split() )
    line = fin.readline().strip()
    game = Game(e, r, n, line)
    
    solution = game.solve()
    print "Case #%d: %d" % (case+1, solution) 
    print "Case #%d: e: %d, r: %d" % (case+1, game.e, game.r )
    print "Case #%d: vi %s" % (case+1, repr(game.v) )
    print "Case #%d: left: %s" % (case+1, repr( game.vi_left() ) ) 


