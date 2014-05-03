import sys

fin = open(sys.argv[1])

N = int( fin.readline().strip() ) 

for _ in range(1, N+1):
    
    C, F, X = map( float,  fin.readline().strip().split() ) 
    
    rate = 1/2.0
    prev = X * rate 
    buy = 1
    while 1:
        currRate = 2 + F * buy 
        post = C * rate + X / currRate 

        if post > prev:
            break
        else:
            prev = post
            buy +=1
            rate += 1/ currRate

    print "Case #%d: %.7f" % (_, prev)
        



