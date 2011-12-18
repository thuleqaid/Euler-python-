def mysum(upper,factor1,factor2):
	x1=(upper-1)/factor1
	x2=(upper-1)/factor2
	x3=(upper-1)/(factor1*factor2)
	ret=x1*(x1+1)*factor1/2+x2*(x2+1)*factor2/2-x3*(x3+1)*factor1*factor2/2
	return ret

if __name__ == '__main__':
	print mysum(1000,3,5)
