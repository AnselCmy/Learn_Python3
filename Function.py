#1,2
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	elif x>0:
		return x
	elif x<0:
		return -x

print(my_abs(-1))
# print(my_abs('a'))


#3
print('-'*10)
def AddAndSub(x, y):
	return x+y, x-y

a, b = AddAndSub(2, 3)
print(a, b)
print(AddAndSub(2,3))


#4
print('-'*10)
def power(x, n=2):
	sum = 1
	while n>0:
		n = n-1
		sum = sum*x
	return sum

print(power(2))
print(power(2, 3))

def Add(n=1):
	n = n+1
	return n
print(Add())
print(Add())
print(Add())

def AddEnd(L = []):
	L.append('end')
	return L
print(AddEnd())
print(AddEnd())
print(AddEnd())


#5
print('-'*10)
def calc(*args):
	sum = 0
	for i in args:
		sum = sum +i*i
	return sum

print(calc(1,2,3))


#6
print('-'*10)
a = 	[1, 2, 3, 4]	
print(calc(*a))


#7,8
print('-'*10)
def person(**kw):
	print(kw)

person(name="Ansel", age=19)

extra = {'name':'Ansel', 'age':19}
person(**extra)


#9
print('-'*10)
def person(name, *, gender, city):
	print(name, gender, city)

person('Ansel', gender='male', city='mianyang')




