import math
import random
# define any function here!
def f(x):
    return x**2

# define any xmin-xmax interval here! (xmin < xmax)
xmin = 0
xmax = 3

# find ymin-ymax
numSteps = 100 # bigger the better but slower!
ymin = f(xmin)
ymax = ymin
for i in range(numSteps):
    x = xmin + (xmax - xmin) * float(i) / numSteps
    y = f(x)
    if y < ymin: ymin = y
    if y > ymax: ymax = y
def area(y, n):
	# Monte Carlo
	rectArea = (xmax - xmin) * (ymax - ymin)
	
	ctr = 0
	for j in range(numSteps):
		x =  random.random()*(xmax-xmin) + xmin
		y =  random.random()*(ymax-ymin)+ymin
		if f(x) > 0 and y > 0 and y <= f(x):
			ctr += 1
		if f(x) < 0 and y < 0 and y >= f(x):
			ctr += 1
	fnArea = rectArea * float(ctr) / numSteps
	print "Area under the curve = " + str(fnArea)
	return fnArea
print area(y,100)



	