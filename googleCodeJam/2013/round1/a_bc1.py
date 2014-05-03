import sys
import pdb
import subprocess
#import math
debug = 0


def solve(r, t):
    # use bc to solve. r, t are string 
    if debug:
        if case == 20:
            pdb.set_trace()
    tmp_exe = 'echo "f('+ r + ',' + t+ ')" | bc -l a.b'
    pipe = subprocess.Popen(tmp_exe, shell=True, stdout = subprocess.PIPE)
    result = int( pipe.stdout.readline() ) 
    return result

fin = open(sys.argv[1])
cases = int( fin.readline() ) 
for case in range(cases):
    
    r, t = fin.readline().split()

    solution = solve(r,t)
    
    #solution = ''
    print "Case #%d: %d" % (case+1, solution) 



