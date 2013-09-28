import sys 

def solve(credit, num_item, items):
    for i in range(num_item):
        if items[i] >= credit: continue
        for j in range(i+1, num_item):
            if items[i] + items[j] == credit:
                return i, j 

f = open(sys.argv[1])
N = int(f.readline())

for i in range(N):
    credit = int(f.readline())
    num_item = int( f.readline() ) 
    items = [ int(j) for j in f.readline().split() ] 

    id1, id2 = solve(credit, num_item, items)
    print "Case #%d: %d %d" %(i+1, id1+1 , id2+1  )

