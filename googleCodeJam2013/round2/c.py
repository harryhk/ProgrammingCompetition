import sys
#import pdb
#import numpy as np 
#import math
debug = 0



fin = open(sys.argv[1])
#fout = open(sys.argv[1]+'.out', 'w')
fin_dict = open('garbled_email_dictionary.txt').readlines()
hash_dict={} # store ( length, word)
for i in fin_dict:
    i=i.strip()

    if hash_dict.has_key(len(i) ):
        hash_dict[len(i) ].append(i)
    else:
        hash_dict[len(i)]=[ i ]
    



cases = int( fin.readline() ) 

for case in range(cases):
    
    s = fin.readline()  

    solution = 2
    print >> fout, "Case #%d: %d" % (case+1, solution) 



