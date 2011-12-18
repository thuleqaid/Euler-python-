def fibo():
	x=1
	y=2
	while y<4000000:
		y+=x
		x=y-x
		yield y

if __name__ == '__main__':
	sum=2
	for item in fibo():
		if item%2==0:
			sum+=item
	print sum
