# making a fraction class 
class Fraction:
	def __init__(self,top,bottom):
		self.check_if_int(top,bottom)
		common = self.gcd(top,bottom)
		self.num = top//common
		self.den = bottom//common


	def check_if_int(self,top,bottom):
		try:
			top += 1
			bottom += 1
		except TypeError:
			print "You entered a non integer...crashing!"
	def show(self):
		print (str(self.num)+"/"+str(self.den))

	def __str__(self):
		return str(self.num)+"/"+str(self.den)

	def gcd(self,m,n):
	    while m%n != 0:
	        oldm = m
	        oldn = n

	        m = oldn
	        n = oldm%oldn
	    return n

	def getNum(self):
		return self.num

	def getDen(self):
		return self.den

	def __eq__(self,other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den

	def __lt__(self,other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den
		return firstnum < secondnum

	def __gt__(self,other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den
		return firstnum > secondnum

	def __add__(self,otherfraction):

		newden = self.den * otherfraction.den
		newnum = self.num*otherfraction.den + self.den*otherfraction.num
		common = self.gcd(newnum,newden)

		return Fraction(newnum//common,newden//common)	

	def __mul__(self,otherfraction):
		newnum = self.num * otherfraction.num
		newden = self.den * otherfraction.den
		common = self.gcd(newnum,newden)

		return Fraction(newnum//common,newden//common)

	def __sub__(self,otherfraction):
		newnum = self.num*otherfraction.den - self.den*otherfraction.num
		newden = self.den * otherfraction.den
		common = self.gcd(newnum,newden)

		return(Fraction(newnum//common,newden//common))

	def reciprocal(self):
		temo = self.num
		self.num = self.den
		self.den = temo
		return (Fraction(self.num,self.den))

	def __div__(self,otherfraction):
		r = otherfraction.reciprocal()
		newnum = self.num*r.num
		newden = self.den*r.den
		common = self.gcd(newnum,newden)

		return(Fraction(newnum//common,newden//common))






		



		