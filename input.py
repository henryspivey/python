import math
anumber = int(input("Please enter a number: "))
if anumber > 0:
	print "The square root is ", math.sqrt(anumber)
else: 
	print ("Bad value for number.")
	print ("Using absolute value instead.")
	print (math.sqrt(abs(anumber)))
