#1
import logging
try:
	print('try... ...')
	r = 10/0
except Exception as e:
	# print('except:', e)
	logging.exception(e)
finally:
	print('finally... ...')

#2
def fn(i):
	if i == 0:
		raise ValueError("can't be zero!")
	else:
		print(10/i)

fn(0)