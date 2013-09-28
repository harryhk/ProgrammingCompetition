
import bisect

flag = 0

def update(l, oper, x):
    global flag
    if oper == 'r':
        try:
            l.remove(x)
        except ValueError:
            flag = 1
    if oper == 'a':
        bisect.insort(l, x)


N= int(raw_input())

l = []

for i in range(0, N):

    tmp = raw_input()
    a, b = [xx for xx in tmp.split()]
    flag = 0
    update(l, a, int(b) )
    
    n = len(l)
    if flag ==1:
        print "Wrong!"
    else:
        if n == 0 :
            print "Wrong!"
        elif  n % 2 ==1:
            print l[ n/2 ]
        elif  n % 2 == 0 :
            t= (l[n/2 -1] + l[n/2])/2.0
            if t == int(t):
                print int(t)
            else:
                print t


