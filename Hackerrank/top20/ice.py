
def solve(s,l):
    for i in range(len(l)):
        for j in range(i, len(l)):
            if s == l[i]+l[j]:
                print i+1, j+1
                break

N = int(raw_input())

for _ in range(N):
    s = int(raw_input())
    l = [ int(i) for i in raw_input().split()]
    solve(s,l)
