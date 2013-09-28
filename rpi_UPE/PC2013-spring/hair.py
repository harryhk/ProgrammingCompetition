import pdb
import sys

f= open(sys.argv[1])
N = int ( f.readline())

def solve():
    k=[0 for i in range(ndays+1)]  # index start at 1 
    L=[0 for i in range(ndays+1)]  # index start at 1 
    Tot=[0 for i in range(ndays+1)]  # index start at 1 
    
    k[1] = M
   
    for nidx in range(2, ndays+1):
        pre_n = 0
        tmp_cost = 1e17
        for i in range(1, nidx):
            tmp_s = k[i] 
            
            for j in range(i+1, nidx):
                if cost.has_key(j): 
                    tmp_s += cost[j] * (j-i)    
            
            if tmp_s < tmp_cost:
                pre_n = i
                tmp_cost = tmp_s

        k[nidx] = tmp_cost + M 
        L[nidx] = pre_n

    for i in range(1, ndays+1):
        Tot[i] = k[i]
        for j in range(i+1, ndays+1):
            if cost.has_key(j):
                Tot[i] += cost[j] * (j-i)
    
    #pdb.set_trace()
    tot_m = min(Tot[1:])
    sd = Tot.index(tot_m)
    q = [sd]
    i = L[sd]
    while i > 0:
        q.append(i)
        i=L[i]

    for i in q[::-1]:
        sys.stdout.write("%s " %i )
    print 

for i in range(N):
    ndays, M , noblis = f.readline().strip().split()
    ndays = int(ndays)
    M = int(M)
    noblis = int(noblis)

    cost = {}
    #pdb.set_trace()
    for i in range(noblis):
        od, ov = f.readline().strip().split()
        if cost.has_key(int(od)):
            cost[int(od)] += int(ov)
        else:
            cost[int(od)] = int(ov)

    solve()
