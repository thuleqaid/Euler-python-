total=1000
for a in range(1,total/3+1):
	for b in range(a+1,(total-a)/2+1):
		c=total-a-b
		if a**2+b**2==c**2:
			print "%d:%d:%d:%d"%(a,b,c,a*b*c)
			break

