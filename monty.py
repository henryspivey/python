import math
import random
M = 1.2247 # maximum y value
a,b = .5, 1.5 # x interval

def area(n):
	counter = 0
	# Check if the y coordinate is above 0 but below the function
	for i in range(0,n):
		# Generate random coordinates between bounds
		rand_x =  random.uniform(a,b)
		rand_y =  random.uniform(0, M)
		if 0.0 <= rand_y and rand_y <= float(math.sqrt(rand_x)):
			counter += 1
	return "Area is ", float(counter)/float(n)


def random_die(n):
	""" Keeps track of the sum of dice """
	sum = 0
	count2 = 0
	count3 = 0
	count4 = 0
	count5 = 0
	count6 = 0
	count7 = 0
	count8 = 0
	count9 = 0
	count10 = 0 
	count11 = 0
	count12 = 0
	for i in range(0,n):
		rand_x = random.randint(1,6)
		rand_y = random.randint(1,6)
		sum = rand_x+ rand_y
	
		if sum == 2:
			count2 += 1
		elif sum == 3:
			count3 += 1
		elif sum == 4:
			count4 += 1
		elif sum == 5:
			count5 += 1
		elif sum == 6:
			count6 += 1
		elif sum == 7:
			count7 += 1
		elif sum == 8:
			count8 += 1
		elif sum == 9:
			count9 += 1
		elif sum == 10:
			count10 += 1
		elif sum == 11:
			count11 += 1
		else:
			count12 += 1
	return "P(2 -> 12) ", float(count2)/float(n), float(count3)/float(n), float(count4)/float(n), float(count5)/float(n),float(count6)/float(n),float(count7)/float(n),float(count8)/float(n),float(count9)/float(n),float(count10)/float(n),float(count11)/float(n),float(count12)/float(n)


for i in range(0,100):
	print random_die(100)

