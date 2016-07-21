#1
a = [x*x for x in range(11)]
print(a)

#2
print('-'*10)
a = [x*x for x in range(11) if x%2==0]
print(a)

#3
print('-'*10)
a = [x+y for x in 'ABC' for y in '123']
print(a)

#4
d = {1:'a', 2:'b', 3:'c'}
a = [str(x)+'='+y for x, y in d.items()]
print(a)