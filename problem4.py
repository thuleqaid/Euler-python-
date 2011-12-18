def isPalindromic(n):
	digits=[i for i in str(n)]
	i,l=0,len(digits)/2
	while i<l:
		if digits[i]!=digits[-(i+1)]:
			return False
		i+=1
	return True

combination=None
upper=1000
while True:
	upper=upper-1
	lower=upper-1
	products=upper*lower
	if combination and products<combination[0]:
		break
	while not isPalindromic(products):
		lower-=1
		products=upper*lower
		if combination and products<combination[0]:
			break
		if lower<100:
			break
	else:
		if (not combination) or products>combination[0]:
			combination=(products,upper,lower)
print combination
