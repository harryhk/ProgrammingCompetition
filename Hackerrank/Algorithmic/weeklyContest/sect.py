from string import maketrans
o="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n="ANBYCODUEPFXGQHVIRJZKSLWMT"
o+=o.lower()
n+=n.lower()
e=maketrans(o,n)
d=maketrans(n,o)
while 1:
	s=raw_input()
	if s[:2]=='DO':
		break
	if s[:2]=='EN':
		print s[7:].translate(e) 
	else:
		print s[7:].translate(d) 
