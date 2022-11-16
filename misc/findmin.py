import time
from random import randrange

def findMin(l):
	# O(n^2)
	# two loops n*n
	temp = l[0]
	
	for i in l:
		for j in l:
			if i>j:
				temp = j
	return temp

def findMin2(l):
	# O(n)
	# one loop
	minsofar = l[0]
	for i in l:
		if i < minsofar:
			minsofar = i
	return minsofar

def findMax(l):
	maxsofar = l[0]
	for i in l:
		if i > maxsofar:
			maxsofar = i
	return maxsofar

l = [5,34,221,10,0]
#print (findMin(l))
print (findMax(l))

"""
for listSize in range(1000,10001,1000):
	l = [randrange(100000) for x in range(listSize)]
	start = time.time()
	print (findMin2(l))
	end = time.time()
	print("Size: %d time: %f" %(listSize,end-start))

"""