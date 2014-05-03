import sys

fin = open(sys.argv[1])
cases = int( fin.readline() ) 

class Game(object):
    def __init__(self, a1, a2, b1, b2):
        self.a1, self.a2, self.b1, self.b2 = a1, a2, b1, b2 

    def _solve(self, i, j ) :
        
        a = max(i,j ) 
        b = min(i,j ) 
        if a >= 2 * b or b==0:
            return True
        else:
            return not self._solve(b, a-b)

    def solve(self):
        count = 0
        for i in range(self.a1, self.a2+1 ) :
            for j in range( self.b1, self.b2 +1 ):
                if self._solve(i, j ):
                    count += 1

        return count


for case in range(cases):
    a1, a2, b1, b2 = map( int, fin.readline().split() ) 
    game = Game(a1, a2, b1, b2)
    solution = game.solve()
    print "Case #%d: %d" % (case+1, solution ) 
