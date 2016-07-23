#1
class Student(object):
	__slots__ = ('name', 'age')
	pass

a = Student()
a.name = "ansel"
a.age = "city"
a.city = 'mianyang'