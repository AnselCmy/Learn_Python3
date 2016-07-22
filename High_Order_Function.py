#1
a = abs
print(a(-10))

#3
print('-'*10)
def add(x, y, f):
	return f(x) + f(y)

print(add(-3, 2, abs))

#4
print('-'*10)
def power(x, n=2):
	sum = 1
	while n>0:
		n = n - 1
		sum  = sum*x
	return sum
L = [1,2,3,4,5,6,7]
a = map(power, L)
print(list(a))

#5
print('-'*10)
from functools import reduce
def add(x, y):
	return x+y

a = reduce(add, L)
print(a) 

#str2int
print('-'*10)
def str2int(s):
	def fn(x, y):
    		return x*10+y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s] #[s] is the index
	return reduce(fn, map(char2num, s)) 

print(str2int('123'))

#
print('-'*10)
def stded(s):
	c1 = s[0].upper()
	c2 = s[1:].lower()
	return c1+c2

L = ['anSEL', 'ERic', 'miCheal']
print(list(map(stded, L)))	

#6
print('-'*10)
def _odd_iter():
	i=1
	while True:
		i=i+2
		yield i

def _not_divisible(n):
	return lambda x: x % n > 0 #return a function

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n 
		it = filter(_not_divisible(n), it)

for n in primes():
	if n<1000:
		print(n)
	else:
		break


#7
print('-'*10)
L = [1, 4, -2, 5, -10, 11]
a = sorted(L, key=abs)
print(a)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def GetScore(x):
	return x[1]
a = sorted(L, key=GetScore, reverse=True)
print(a)


