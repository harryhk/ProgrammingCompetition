import sys
#import pdb
#import math
debug = 0

vowerls=set(['a','e', 'i', 'o', 'u'])

def is_ok(s):
    for i in s:
        if i in vowerls:
            return False

    return True

def solve(string, n ):
    l=len(string)
    indexes = []
    for i in range(l-n+1):
        j = i+n    
        if len( indexes) !=0:
            j_pre = indexes[-1][1]
            if string[j-1] not in vowerls and  j == j_pre +1:
                indexes.append(( i,j) )
                continue

        if is_ok(string[i:j] ):
            indexes.append((i,j ) )
    if len(indexes) == 0 :
        return 0
    num = [ 0 for _ in range(len(indexes)) ]
    i = indexes[0][0]
    j = indexes[0][1]
    num[0] =  (i+1) * (l-j +1)

    for index in range(1, len(num)):
        ii_pre, jj_pre = indexes[index-1]
        ii, jj = indexes[index]

        num[index] = (ii - ii_pre) * (l - jj +1)
    return sum(num)

fin = open(sys.argv[1])
cases = int( fin.readline() ) 
for case in range(cases):
    
    string, n = fin.readline().split()
    n = int(n) 

    solution = solve(string, n )
    
    print "Case #%d: %d" % (case+1, solution) 



