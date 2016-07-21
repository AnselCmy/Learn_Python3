#1,2
L = [1, 2, 3, 4, 5]
T = ('a', 'b', 'c', 'd', 'e')
print('len(L) = %d' % len(L))
print('len(T) = %d' % len(T))

#3
print('-'*10)
print('L[-1] = %d' % L[-1])

#4
print('-'*10)
L.append(6)
print(L)

#5
print('-'*10)
L.pop()
print(L)
L.pop(1)
print(L)

#6
a = [1, 2, T, 4]
print(a[2][2])

#7
b = [1, 'c', 1.23]
print(b)