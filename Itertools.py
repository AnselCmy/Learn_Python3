import itertools
#1
print('-'*10)
nt = itertools.count(1)
# for i in nt:
#     print(i)

#2
print('-'*10)
cs = itertools.cycle([1,2,3])
# for i in cs:
    # print(i)

#3
print('-'*10)
ns = itertools.repeat('A',3)
for i in ns:
    print(i)

#4
print('-'*10)
nt = itertools.count(3)
ns = itertools.takewhile(lambda x: x<=10, nt)
print(list(ns))

#5
print('-'*10)
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

#6
print('-'*10)
for key, group in itertools.groupby("AAaBbBcCc", lambda c: c.upper()):
    print(key, list(group))