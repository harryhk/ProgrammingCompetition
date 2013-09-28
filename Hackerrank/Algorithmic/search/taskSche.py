import bisect

def max_time(l ):
    time = 0
    max_wait = 0
    for i in l:
        time += i[1] 
        tmp = time - i[0]
        if max_wait < tmp:
            max_wait = tmp
            dindx = i
    return max_wait


N = int( input() ) 
task = []
dindx =None
for i in range(N):
    a, b = raw_input().strip().split()
        
    a = int(a)
    b = int(b)
    bisect.insort(task, (a,b))

    max_wait, dindx=  max_time(task, dindx )
