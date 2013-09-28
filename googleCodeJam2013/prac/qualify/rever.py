import sys 

d={}
d['2']='abc'
d['3']='def'
d['4']='ghi'
d['5']='jkl'
d['6']='mno'
d['7']=


def solve(line):
    


f = open(sys.argv[1])
N = int(f.readline())

for i in range(N):
    line = f.readline()
    
    print "Case #%d: %s" %(i+1,  solve(line) )

