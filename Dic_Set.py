#1,2
D = {'a':1, 'b':2, 'c':3, 'd':4}
print(D)
print("D['a'] = %d" % D['a'])

#3
print('-'*10)
L1 = [2,1,5,7,2]
L2 = [7,9,0,1,2,]
S1 = set(L1)
S2 = set(L2)
print('S1 = %s' % S1)
print('S2 = %s' % S2)

#4
print('-'*10)
print('S1|S2 = %s' % (S1|S2))
print('S1&S2 = %s' % (S1&S2))
print('S1^S2 = %s' % (S1^S2))