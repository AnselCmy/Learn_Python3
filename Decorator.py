import functools
#1
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print("call %s()" % func.__name__)
		return func(*args, **kw)
	return wrapper

@log #now = log(now)
def now():
	print('2016-7-22')

now()

#2
print('-'*10)
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s()' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log('fuck') #now = log('fuck')(now)
def now():
	print('2016-7-22')

now()
print(now.__name__)