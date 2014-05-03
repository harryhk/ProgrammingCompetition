import sys
import subprocess

def solv(n):
    tmp_exe = 'echo "f(' +n + ')" | bc -l c.b' 
    result = subprocess.check_output(tmp_exe, shell=True)
    result = result.strip()
    result = '000' + result
    idx = result.index('.')
    return result[idx-3:idx ]


fin = open(sys.argv[1])
cases = int( fin.readline() ) 

for case in range(cases):
    
    n = fin.readline().strip()  
    solution = solv(n)
    print "Case #%d: %s" % (case+1, solution) 
