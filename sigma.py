def sigma3and5():
	sigma = 0
	for i in range(1,1000):
		if i%3 == 0 or i%5 == 0:
			sigma += i
	return sigma

# print(sigma3and5())


def even_Fibonacci():
	lh = 0
	rh =  1
	newsum = 0
	fs= 0
	while fs < 4000000:
		fs = lh + rh
		lh  = rh
		rh = fs

		if fs%2 == 0:
			newsum+=fs
	return newsum
		

# print(even_Fibonacci())



