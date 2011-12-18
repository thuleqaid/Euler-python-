import math
def isPrime(primelist,num):
	upper=math.sqrt(num)
	for item in primelist:
		if item>upper:
			return True
		if num%item==0:
			break
	return False
plist=[2,3]
count=10001
i=3
while len(plist)<count:
	i+=1
	if isPrime(plist,i):
		plist.append(i)
print plist[-1]
