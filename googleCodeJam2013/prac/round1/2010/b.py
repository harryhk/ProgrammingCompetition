import sys, math
import pdb

debug = 0

class Game(object):
    def __init__(self, d, i, m, na, line):
        self.d, self.i, self.m, self.na = d, i, m, na
        self.ai =  map( int, line.split() ) 
        self.cost = [ 0 for _ in range(257) ] 
        for i in range(256):
            self.cost[i] = abs( self.ai[0] - i )
        
        self.cost[256] = self.d 

    def solve(self):
        if (self.d == 0 or  self.i == 0) and self.m !=0:
            return 0
        
        if debug:
            if case ==4:
                pdb.set_trace()
        
        for ni in range(1, self.na):
            self.cost_next = [ 0 for _ in range(257) ] 
            for p_i in range( 256 ) :
                c_ap = abs( p_i - self.ai[ni] ) 
                best = self.cost[256] + c_ap
                for q_i in range( 256) :
                    if abs( p_i - q_i ) <= self.m:
                        best = min( best, self.cost[q_i] + c_ap )
                    else:
                        if self.m != 0: 
                            tmp = self.cost[q_i] + ( abs( p_i - q_i ) - 1 ) / self.m * self.i + c_ap

                            best = min(best, tmp) 
                self.cost_next[p_i] = min( best, self.cost[p_i] + self.d )
            self.cost_next[256] = self.cost[256] + self.d 
            self.cost = self.cost_next[:]
                        
        return min(self.cost)


fin = open(sys.argv[1])
cases = int( fin.readline() ) 

for case in range(cases):
    
    d,i,m,na = map(int, fin.readline().split() )
    game = Game( d,i, m, na, fin.readline().strip() )
    solution = game.solve()
    print "Case #%d: %d" % (case+1, solution)
