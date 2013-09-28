import pdb
def stockM(d):
    nd =len(d)+1
    for i in range(1, nd):
        pdb.set_trace()
        if i==1:
            li=[0]*(i+1)
            li[0]=0
            li[1]=-d[i-1]
            continue
        else:
            lii=[0]*(i+1)
            for n in range(i+1):
                tmp=-1e17
                for m in range(n, i):
                    tmp= max( li[m] + d[i-1]*(m-n), tmp)
                if n >0:
                    tmp = max( tmp, li[n-1] - d[i-1] )
                lii[n] = tmp
        li=lii[:]

    print int(max(lii))
        

N=int( raw_input() ) 
for i in range(N):
    nd = raw_input()
    d = [ int(i) for i in raw_input().split() ]
    stockM( d )
