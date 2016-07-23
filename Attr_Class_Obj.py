#1
class Student(object):
	def __init__(self, name):
		self.name = name
	def set_city(self, city):
		self.city = city

ansel = Student('Ansel')
ansel.set_city('mianyang')
print(ansel.city)

ansel.age = 19
print(ansel.age)


#2
print('-'*10)
class Teacher(object):
	job = "Teacher"

hua = Teacher()
print(hua.job)