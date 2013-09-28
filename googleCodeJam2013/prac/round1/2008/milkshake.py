import sys
import pdb

debug = 0

def unsatisfy(cus, milk_malt, milk_unmalt, flag_never_satisfy):
    tmp_malt = set(cus.malt) & milk_malt
    tmp_unmalt = cus.unmalt & milk_unmalt


    if tmp_malt or tmp_unmalt:
        return False

    if len(cus.malt) == 0 and len( tmp_unmalt ) ==0:
        flag_never_satisfy[0] = True
        return True 

    milk_unmalt.remove(cus.malt[0])
    milk_malt.add( cus.malt[0])
    return True

def solve():
    milk_unmalt = set( range(1, n_flavor+1) )
    milk_malt = set()

    flag_satisfy = True
    flag_never_satisfy = [False]
    
    if debug:
        pdb.set_trace()
    while customers:
        
        for cus in customers:
            if  unsatisfy(cus, milk_malt, milk_unmalt, flag_never_satisfy):
                if flag_never_satisfy[0]:
                    return False
                else:
                    flag_satisfy = False
                    break

        
        if flag_satisfy:
            return map( lambda x: 1 if x in milk_malt else 0, range(1, n_flavor+1) )
        else:
            customers.remove(cus) 
            flag_satisfy = True

    return  map( lambda x: 1 if x in milk_malt else 0, range(1, n_flavor+1) )
    
    
        

class Customer(object):
    def __init__(self, line):
        line = map( int, line.strip().split())
        self.likes = [ (line[2*i+1], line[2*i+2] )  for i in range(line[0]) ]
        
        self.unmalt = set( [ i for i, j in self.likes if j==0 ]  )
        self.malt = [ i for i, j in self.likes if j==1]

    def __repr__(self):
        return "<%s, %s>" % ( repr(self.unmalt) , repr(self.malt) )
        

fin = open(sys.argv[1])
cases = int( fin.readline() ) 
for case in range(cases):
    
    n_flavor = int( fin.readline() )
    n_customer = int( fin.readline() )
    
    customers = []
    for _ in range(n_customer  ):
        customers.append( Customer(fin.readline() ) )

    solution = solve()
    if solution :
        solution = ' '.join(map(str, solution ))
    else:
        solution = 'IMPOSSIBLE'
    print "Case #%d: %s" % (case+1, solution) 
