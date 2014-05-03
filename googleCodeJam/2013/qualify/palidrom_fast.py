import sys 
import numpy as np 

def palindrom_n(palindromes , n):
    # generate palidrom with n digits 
    l=[]
    for i in range(10): 
        for j in palindromes[n-2]:
            l.append( str(i) + j  + str(i)  )

    return l
        

def palid(num):
    num_s = str(num)
    return num_s == num_s[::-1]


def solve( palin_list,  n, m):
    count = 0 
    n_s = int( np.sqrt(n) ) if np.sqrt(n) == int(np.sqrt(n)) else int(np.sqrt(n)) +1
    m_s = int( np.sqrt(m) )

    p_list = [ i for i in palin_list if i>= n_s and i<= m_s  ]
    
    #print p_list
    
    for i in p_list:
        ii= i*i
        if palid(ii):
            #print i , ii
            count +=1 

    return count
    
    

            

palindromes = {}
palindromes[1]=['0','1','2','3','4','5','6','7','8','9']
palindromes[2]=['00', '11','22','33','44','55','66','77','88','99']
for i in range(3,8):
    palindromes[i] = palindrom_n( palindromes, i)
    

palin_list = []
for i in palindromes:
    palin_list += [ int(j) for j in palindromes[i] if j[0] !='0' ]

palin_list.sort()

#for i in palin_list:
#    print i
#sys.exit(1)

f = open(sys.argv[1])
N = int(f.readline())

for i in range(N):
    n, m = f.readline().split()
    n, m = ( int(n), int(m)  )

    
    print "Case #%d: %s" %( i+1, solve(palin_list, n, m) )
