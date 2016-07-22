class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def set_name(self, name):
		self.__name = name

	def get_name(self, name):
		return self.__name

	def print_info(self):
		print('%s,%d' % (self.__name, self.__score))

Ansel = Student('Ansel', 100)
Ansel.set_name('Ansel_Chen')
Ansel.print_info()
