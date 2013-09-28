#!/bin/python

import pdb

def triplets(ar):
        
    tups=[0]*len(ar)
    tups_list=[ [] for i in range(len(ar)) ] 
    trips = [0] *len(ar)
    for i in range(len(ar)):
        temp = set()
        #pdb.set_trace()
        for j, j_val in enumerate(ar[:i]):
            if j_val < ar[i]:
                temp.add(j_val)
                tups_list[i].append(j)
        
        #print tups_list
        tups[i] = len(temp) 
        #tups[i] =  len( set( [j for j in ar[:i] if j < ar[i] ] ) ) 
	
   
    for i in range(len(ar)):
        d={}
        #for j, j_v in enumerate(ar[:i+1]):
        for j in tups_list[i]:
            #j_v = ar[j]
            #if j_v < ar[i]:
            d[ar[j]] = tups[j]
        
        trips[i] = sum(d.values())
    
    d={}
    for i in range(len(ar)):
        d[ar[i]] = trips[i]
    
    print sum(d.values())

# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
triplets(ar) 
