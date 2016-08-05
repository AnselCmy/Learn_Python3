#1
from collections import namedtuple

Point = namedtuple('PointTuple', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x)
print(p.y)

#2
print('-'*10)
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('-a')
print(q)
q.pop()
q.popleft()
print(q)

#3
print('-'*10)
from collections import defaultdict
d = defaultdict(lambda: 'NULL')
print(d['a'])

#4
print('-'*10)
from collections import OrderedDict
l = list(zip(('a','b','c'), (1,2,3)))
d = OrderedDict(l)
print(d)

#5
print("-"*10)
from collections import Counter
c = Counter()
for i in 'my life is brilliant':
    c[i] += 1

print(c)