def factor(n):
	outs={}
	x=2
	while x<n:
		while n%x==0:
			if x in outs:
				outs[x]+=1
			else:
				outs[x]=1
			n=n/x
		x+=1
	outs[n]=1
	return outs

if __name__ == '__main__':
	print max(factor(600851475143).keys())

