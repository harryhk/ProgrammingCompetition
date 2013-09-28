import sys
import itertools
import pdb
#import numpy as np 

debug = 0

class Guess(object):
    def __init__(self,  r,n,m,k, line):
        self.r, self.n, self.m, self.k = r,n,m,k 
        self.products = map( int, line.split() ) 
        self.products = set( self.products) 

    def is_solution(self, candidate):
        tmp_products = self.products.copy()

        for i in range(1, self.n+1):
            for j in itertools.combinations(candidate, i  ):
                prod = reduce(lambda x,y: x*y, j )
                if prod in tmp_products:
                    tmp_products.remove(prod)
                    if len(tmp_products) == 0:
                        return True

        return False


    def solve(self):
        self.candidates = list(itertools.combinations_with_replacement( range(2, self.m+1), self.n )) 
        
        tmp = [  (i, len(set(i)) )  for i in self.candidates ]
        tmp.sort( key = lambda x: -x[1] )
        self.candidates = tmp 

        if debug:
            pdb.set_trace()

        if len( self.products - set([1]) ) == 0  :
            candidate = self.candidates[0][0]
            return ''.join(map(str,  candidate) )
        else:
            self.products = self.products - set([1])

        for candidate, _ in  self.candidates :
            if self.is_solution(candidate):
                return ''.join(map(str,  candidate) )
        
        return ''


fin = open(sys.argv[1])
cases = int( fin.readline() ) 
for case in range(cases):
    
    print 'Case #%d:' % (case+1)
    r, n , m, k = map(int, fin.readline().split() )
    for _ in range(r):
        line= fin.readline().strip()
        guess =Guess(r, n, m, k , line)
        solution = guess.solve()
        print '%s' % solution
    
    



