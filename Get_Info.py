#1
class Animal(object):
	def run(self):
		print("Animal is running!")

class Dog(Animal):
	def run(self):
		print("Dog is running!")

class Cat(Animal):
	def run(self):
		print("Cat is running!")


a = Animal()
d = Dog()
c = Cat()

print(type(a))

#2
print('-'*10)
import types
def fn():
	pass
f = type(fn) == types.FunctionType
print(f)

#3
print('-'*10)
print(isinstance(c, Cat))
print(isinstance(c, Animal))

#4
print('-'*10)
print(dir(a))

#5
print('-'*10)
s = 'ABC'
print(len(s))
print(s.__len__())

#6
print('-'*10)
class person(object):
	def __init__(self, name="None", age=0):
		self.name = name
		self.age = age

	def print_info(self):
		print(self.name, self.age)
	
	#attribute
ansel = person('Ansel', 19) 
ansel.print_info()
print(getattr(ansel, 'name'))
print(getattr(ansel, 'city', 'no attr'))

print(hasattr(ansel, 'age'))

setattr(ansel, 'name', 'chen')
print(getattr(ansel, 'name'))
	
	#method
print(hasattr(ansel, 'print_info'))
fn = getattr(ansel, 'print_info')
fn()

#
print('-'*10)
print(hasattr('ABC', 'len'))
print(hasattr('ABC', '__len__'))