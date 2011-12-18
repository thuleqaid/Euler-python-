def isPrime(primelist,num):
	upper=num**0.5
	for item in primelist:
		if item>upper:
			return True
		if num%item==0:
			break
	return False
def primelist(n):
	plist=[2,3]
	i=5
	while i<n:
		if isPrime(plist,i):
			plist.append(i)
		i+=2
	return plist
print sum(primelist(2000000))
