import sys

fin = open(sys.argv[1])
N = int(fin.readline())
for _ in range(N):
    fin.readline()
    x = map( int , fin.readline().split() )
    y = map( int , fin.readline().split() )
    print "Case #%d: %d" %( _+1,    sum( [ xx * yy for xx, yy in zip( sorted(x) , sorted(y, reverse=True)  ) ]  ) )

