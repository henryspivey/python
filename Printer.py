import random

class Printer:
	"""simulation of a printer using a queue"""
	def __init__(self, ppm):
		self.pagerate  = ppm
		self.currentTask = None
		self.timeRemaining = 0

	def tick(self):
		if self.currentTask != None:
			self.timeRemaining -= 1
			if self.timeRemaining <= 0:
				self.currentTask = None
	def busy(self):
		if self.currentTask != None:
			return True
		else:
			return False
	def startNext(self, newTask):
		self.currentTask = newTask
		self.timeRemaining = newTask.getPages()*60/self.pagerate

class Task:
	def __init__(self, time):
		self.timeStamp = time
		self.pages = random.randrange(1,21)

	def getStamp(self):
		return self.timeStamp

	def getPages(self):
		return self.pages

	def waitTime(self, currenttime):
		return currenttime - self.timeStamp
		