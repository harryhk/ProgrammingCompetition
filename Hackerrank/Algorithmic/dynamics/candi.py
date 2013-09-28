N = raw_input()
N= int(N)
l=[]
for i in range(N):
    l.append( (int(raw_input().strip() ) , i) )

ls = sorted(l)
candi = [1] * N
for i in range(N):
    d=ls[i]
    ii = d[1]
    il= ii -1
    ir= ii +1
    if ii ==0:
        b=1e17
        e=l[ir][0]
    elif ii == N-1:
        b=l[il][0]
        e = 1e17
    else:
        b=l[il ][0]
        e=l[ir][0]
   
    if d[0] > b and candi[ii] <= candi[il]:
        candi[ ii ] = candi[ il ] +1
    if d[0] > e and candi[ii] <= candi[ir] :
        candi[ ii ] = candi[ ir ]+1

print sum(candi)
