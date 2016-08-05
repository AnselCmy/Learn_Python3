from datetime import datetime
#1
print('-'*10)
print(datetime.now())

#2
print('-'*10)
print(datetime(2016,8,26,13,10))

#3
print('-'*10)
dt = datetime(2016,8,26,13,10)
print(dt.timestamp())

#4
print('-'*10)
t = dt.timestamp()
print(datetime.fromtimestamp(t))

#5
print('-'*10)
cday = datetime.strptime('2016-8-26 13:10:59', '%Y-%m-%d %H:%M:%S')
print(cday)

#6
print('-'*10)
now = datetime.now()
timestr = now.strftime('%a, %b %d, %H:%M')
print(timestr)