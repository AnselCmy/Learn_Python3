#1
for i in 'Ansel':
	print(i)

#2
print('-'*10)
d = {'a':1, 'b':2, 'c':3, 'd':4}
for i in d:
	print(i)

#3
print('-'*10)
for v in d.values():
	print(v)


#4
print('-'*10)
for x, y in d.items():
	print(x, y)

#6
print('-'*10)
L = ['my', 'life', 'is', 'brilliant']
for x, y in enumerate(L):
	print(x, y)

#7
L = [(1,2),(3,4),(5,6)]
for x, y in L:
	print(x, y)