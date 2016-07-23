#1
class Student(object):
	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be int!')
		if value < 0 or value > 100:
			raise ValueError('score must <0 or >100')	
		self._score  = value

s = Student()
s.score = 100
print(s.score)

#2
print('-'*10)
class Student(object):
	@property
	def score(self):
		return self._score
	
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be int!')
		if value < 0 or value > 100:
			raise ValueError('score must <0 or >100')	
		self._score  = value

	@property
	def level(self):
		if self._score >= 60:
			return 'A'
		else:
			return 'B'

s = Student()
s.score = 59
# s.level = 'A'
print(s.level)