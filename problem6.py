def sumsquare(n):
	data=range(1,n+1)
	s=sum(data)
	return s*s
def squaresum(n):
	data=[i*i for i in range(1,n+1)]
	s=sum(data)
	return s

n=100
print sumsquare(n)-squaresum(n)
