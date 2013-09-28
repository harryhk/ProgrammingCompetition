N, K = raw_input().split()
N = int(N)
K = int(K)
prices= [ int(i) for i in raw_input().split()]
prices.sort(reverse=True)

s=0
for i ,j in enumerate(prices):
    s += ( i/ k +1 ) * j 

print s 

