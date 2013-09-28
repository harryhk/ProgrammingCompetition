#!/bin/python
def partition(ar):    
   	ll= [ i for i in ar[1:] if i <= ar[0]    ]
	lr= [ i for i in ar[1:] if i > ar[0]    ]
	ll.append(ar[0] )
	ll.extend(lr)

	print "".join( "%s " %  i for i in ll   )




# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
