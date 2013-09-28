n=int( raw_input() ) 
for i in range(n):
	d=[  int(i) for i in  raw_input().split() ]
	s=sum(d)
	c, j=(0,0)
	while c<9:
		if d[j] ==10:
			s=s+d[j+1]+d[j+2]
			j+=1
		elif d[j]+d[j+1] ==10:
			s+=d[j+2]
			j+=2
		else:
			j+=2
		c+=1
	print s
