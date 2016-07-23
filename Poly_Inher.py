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
a.run()
d.run()
c.run()

#2
print('-'*10)
def make_run(animal):
	animal.run()

make_run(a)
make_run(d)
make_run(c)

class Rabbit(object):
	def run(self):
		print('Rabbit is running fast!')

r = Rabbit()
make_run(r)