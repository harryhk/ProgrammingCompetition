#!/bin/python

# Head ends here
def insertionSort(ar):    
    for i in range(1, len(ar)):
		insertSub(ar, i)
		print  ''.join( [ '%s ' % (j) for j in  ar]) 



def insertSub( ar, index  ):
	# insert sort ar[0:index-1], ar[index]
	temp = ar[index]
	i=index 
	while i>0:
		if ar[i-1] > temp :
			ar[i] = ar[i-1]
		else:
			ar[i] = temp
			break
		i=i-1
	
	if i==0:
		ar[i] = temp 


# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
