import sys
import pdb

def disjoint_set(l, lsum):
    l.sort(key=lambda x:x[1]) # sort with ending index
    p = [ -1 for i in range(len(l)) ]
    m_sets = [ 0 for i in range(len(l))  ]
    m_sets[0]=1
    
    for i in range( len(l))[::-1]:
        b = l[i][0]
        j = i-1
        while j>=0: 
            if l[j][1] < b:
                p[i] = j
                break    
            j-=1

    for i in range(1, len(l) ):
        if p[i] != -1:
            m_sets[i] = m_sets[ p[i] ]+1
        else:
            m_sets[i] =1
    #if lsum ==7:
    #    print "P", p
    #    print "m_sets", m_sets
    return max( m_sets )


f = open(sys.argv[1])

N = int( f.readline())

#pdb.set_trace()
for ni in range(N):
    L=[]
    ntot = int( f.readline() ) 
    for i in range(ntot):
        L.append(int(f.readline()) )
    
    if ni >-1:
        s=sum(L)
        count = [ 0 for  j in range(s+1)]

        count_list= [ [] for i in range(s+1)  ]
        
        
        for ii in range(ntot):
            for jj in range(ii+1, ntot+1):
                set_sum= sum(L[ii:jj]) 
                count_list[set_sum].append( (ii, jj-1) )
        

        for i in range(1, s+1):
            if len(count_list[i]) >0:
                count[i] = disjoint_set( count_list[i], i )
        
        #print len(count_list[10]) ,count_list[10]

        #print "L", L 
        print max(count) 
        
