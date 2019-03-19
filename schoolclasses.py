class Person:

	def __init__(self,n):
		self.name = n
		self.teaches = None

	def getName(self):
		return self.name

	def canTeach(self):
		self.teaches = self.analiseperson()
		return self.teaches

class Teacher(Person):

	def __init__(self,n):
		Person.__init__(self,n)
	
	def analiseperson(self):
		self.teaches = 1
		if self.teaches:
			print(self.getName()+" can teach.")
		return self.teaches
		


def main():
	t= Teacher("Sue")
	n = t.getName()
	print("The teacher's name is",n)
	print(t.canTeach())

main()