def mytest(mysol, i, j ):
	if mysol.find(i) - mysol.find(j) <= 0 : 
		return 0
	else:
		return 1 


mysol=   open('mysol','r').readline().strip()

constraint =  [i.strip()    for i in  open('t','r').readlines()]
c = 0 
for i in constraint:
	for j in range(len(i)-1):
		for k in range( j+1, len(i) ):
			if mytest(mysol, i[j], i[k]) > 0:
				print c, i, i[j], i[k] ,  "fail"
				break 
	c+=1
