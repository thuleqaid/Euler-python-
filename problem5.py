import operator
def moddiv(x,y):
	if x%y==0:
		return x/y
	else:
		return x
def getnum(n):
	data=range(1,n+1)
	outs=[]
	n=2
	while n<=max(data):
		mod=[i%n for i in data]
		if 0 in mod:
			outs.append(n)
			data=[moddiv(i,n) for i in data]
		else:
			n+=1
	return outs

print reduce(operator.mul,getnum(20))
