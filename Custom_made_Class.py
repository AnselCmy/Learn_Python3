#1
class Student(object):
	def __str__(self):
		return 'Student object (name:%s)' % self.name
	__repr__ = __str__
	def __init__(self, name):
		self.name = name

s = Student('Ansel')
print(s)

#2
print('-'*10)
class Fib():
	def __init__(self):
		self.a = 0
		self.b = 1

	def __iter__(self):
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a+self.b
		if self.a>100:
			raise StopIteration()
		return self.a

for i in Fib():
	print(i)

#3
print('-'*10)
class Fib():
	def __getitem__(self, n): #n is the index
		a, b = 1, 1
		for i in range(n):
			a, b = b, a+b
		return a

f = Fib()
print(f[5])

#4
print('-'*10)
class person():
	def __init__(self, name):
		self._name = name

	def __call__(self):
		print('%s' % self._name)

s = person('Ansel')
s()

