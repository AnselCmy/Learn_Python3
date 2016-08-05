import re
#1
print('-'*10)
test = '0816-2360205'
expr = r'\d{3,4}\-\d{7}'
if re.match(expr, test):
    print("ture")
else:
    print("false")

#2
print('-'*10)
test = 'a,b, c;d  e'
print(re.split(r'[\s\,\;]+', test))

#3
print('-'*10)
test = '0816-2360205'
expr = r'(\d{3,4})\-(\d{7})'
m = re.match(expr, test)
print(m.group(0))
print(m.group(1))
print(m.group(2))