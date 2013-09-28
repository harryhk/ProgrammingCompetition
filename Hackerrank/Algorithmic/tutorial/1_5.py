#!/bin/python

def quickSort(ar):
	if len(ar) <= 1:
		return ar 
	else:
		ll=[ i for i in ar[1:] if i <= ar[0] ]
		lr=[ i for i in ar[1:] if i > ar[0]  ]

		if type(ll) != list:
			ll=[ll]
		if type(lr) != list:
			lr=[lr]
		
		ll=quickSort(ll)
		lr=quickSort(lr)
		print "".join([ "%s " % (i) for i in  ll+[ar[0]] + lr] ) 
		return ll+[ar[0]] + lr



# Tail starts here

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)
