import sys

class Case(object):
    def __init__(self, i, j, diff):
        self.index= (i,j)
        self.diff = diff
    def __lt__(self, other):
        return self.diff < other.diff
        
    def __repr__(self):
        return "(%d, %d): %d" % (self.index[0], self.index[1], self.diff)
            


def solve(v1, v2, v_n):
    rank = []
    for i in range(v_n):
        for j in range(i+1, v_n):
            diff = v1[j]*v2[i] + v1[i]*v2[j] - v1[i]*v2[i] - v1[j]*v2[j]
            rank.append( Case(i, j , diff)  )

    rank.sort()
   
    if rank and rank[0].diff < 0:
        i ,j = rank[0].index
        tmp = v1[ i ]
        v1[i] = v1[j]
        v1[j] = tmp
    
    rank = []
    for i in range(v_n):
        for j in range(i+1, v_n):
            diff = v1[j]*v2[i] + v1[i]*v2[j] - v1[i]*v2[i] - v1[j]*v2[j]
            rank.append( Case(i, j , diff)  )
    
    rank.sort()
   
    if rank and rank[0].diff < 0:
        i ,j = rank[0].index
        tmp = v1[ i ]
        v1[i] = v1[j]
        v1[j] = tmp

    
    return sum( [ i*j for i , j in zip(v1, v2) ] )
    


f=open(sys.argv[1])
N = int( f.readline())

for i_N in range(N):
    v_n = int( f.readline())
    v1 = [ int(i) for i in f.readline().split()  ]
    v2 = [ int(i) for i in f.readline().split()  ]

    print "Case #%d: %d" %( i_N+1, solve(v1, v2, v_n))
