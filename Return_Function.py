#1
def lazy_sum(*args):
	def sum():
		s = 0
		for i in args:
			s = s + i
		return s
	return sum

f = lazy_sum(1, 2, 3)
print(f)
print(f())

#2
print('-'*10)
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())

def count():
	def f(i):
		def g():
			return i*i
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())