import sys
import math
debug = 0



def solve(x, y , movex, movey):
    step=1
    path=''
    remainx = x
    while remainx > 0:
        remainx -= step 
        path += movex[0]
        step += 1

    remainx = - remainx 
    for i in range(remainx):
        path +=movex[0] + movex[1]
        step += 2

    remainy = y 
    while remainy > 0:
        remainy -= step
        path += movey[0]
        step +=1
    remainy = -remainy
    for i in range(remainy):
        path +=movey[0] + movey[1]
        step += 2

    return path

fin = open(sys.argv[1])
cases = int( fin.readline() ) 
move_x = ( ('E','W'), ('W','E') )
move_y = ( ('N','S'), ('S','N'))
for case in range(cases):
    
    x, y = map(int, fin.readline().split()  )
    movex = move_x[0]
    movey = move_y[0]
    if x <0:
        movex = move_x[1]
        x = -x
    if y < 0:
        movey = move_y[1]
        y = -y 
    solution = solve(x,y, movex, movey) 

    
    print "Case #%d: %s" % (case+1, solution) 



