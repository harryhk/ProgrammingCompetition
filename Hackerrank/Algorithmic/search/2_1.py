#!/bin/python

def count_diff(ar, k):
	ar.sort()
	n=0
	for i in range(len(ar)-1):
		j = i+1
		while j!=len(ar) and   ar[j] <= ar[i]+k:
			if ar[j] == ar[i]+k:
				n=n+1
			j = j+1
			
	print n




# Tail starts here

m, k = [ int(i) for i in raw_input().strip().split()]
ar = [int(i) for i in raw_input().strip().split()]
count_diff(ar, k) 
