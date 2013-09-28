#import pdb
def triplets(ar):
    sort_ar=[(0,0)]*len(ar)  
    trips = [0] *len(ar)
    
    sort_ar[0] = ( ar[0], 0 ) 
    trips[0]=0
    l_sort_ar=1  # length of sort_ar
    for i in range(1,len(ar)):
        # start binary sort  
        #pdb.set_trace()
        fi=0
        li=l_sort_ar
        found=0
        while li - fi > 0:
            mi = (li+fi)/2
            if ar[i] > sort_ar[mi][0]:
                fi = mi+1
            elif ar[i] < sort_ar[mi][0]:
                li = mi 
            else:
                found=1
                li = mi 
                break 
        if found==0:  # insert before li
            j = l_sort_ar
            while j > li:
                sort_ar[j] = sort_ar[j-1]
                j -=1
            l_sort_ar += 1
            sort_ar[j] =  (  ar[i] , li  )
        else:
            sort_ar[mi] = (  ar[i] , mi  ) 
        trips[i]=0
        j = 0
        while j < li:
            trips[i] += sort_ar[j][1]
            j+=1

        
        #tups[i] =  len( set( [j for j in ar[:i] if j < ar[i] ] ) ) 
    #print tups
    
    d={}
    for i in range(len(ar)):
        d[ar[i]] = trips[i]
    
    print sum(d.values())

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
triplets(ar) 
