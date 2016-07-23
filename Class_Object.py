class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
	    self.name = name
		self.score = score

	def PrintInfo(self):
		print('%s,%d' % (self.name, self.score))
	
Ansel = Student('Ansel', 100)

Ansel.PrintInfo()		