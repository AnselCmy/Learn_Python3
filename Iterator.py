from collections import Iterator

#1
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))

#2
print('-'*10)
print(isinstance(iter([]), Iterator))