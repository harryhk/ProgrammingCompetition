import sys 
from itertools import combinations

def switch_code(dev, out):
    
    r=''
    for i , j in zip(dev, out) :
        if i==j:
            r+='0'
        else:
            r+='1'
    return r


def solve(device, outlet, N, L):
    
    n =1 

    for dev in device:
        tmp = set()
        for out in outlet:
            tmp.add( switch_code(dev, out)  )
        if n== 1:
            switch_map = tmp 
            n =2 

        else:
            switch_map = switch_map & tmp 

    if len(switch_map) == 0 :
        return -1
    else:
        tmp = [ sum( map(int, i) ) for i in switch_map  ]
        return sorted(tmp)[0]


f = open(sys.argv[1])
cases = int( f.readline().strip()  )

for case in range(1, cases+1):
    
    N, L = map(int, f.readline().strip().split() )

    device = f.readline().strip().split()
    outlet = f.readline().strip().split() 

    ans = solve(device, outlet, N, L )
    if ans < 0:
        print "Case #%d: NOT POSSIBLE" % case
    else:
        print "Case #%d: %d" % ( case, ans ) 
