class counter:
	count = 0
	def __init__(self):
		self.__class__.count += 1
	def reveal_count(self):
		return self.__class__.count
