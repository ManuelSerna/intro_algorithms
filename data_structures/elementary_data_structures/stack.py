#************************************************
# Stack class
# Note: LIFO
#************************************************

class Stack():
	def __init__(self):
		self.top = 0
		self.S = []

	def empty(self):
		if self.top == 0:
			return True
		else:
			return False

	def push(self, x):
		self.top += 1
		self.S.append(x) # No need to check for overflow

	def pop(self):
		if self.empty():
			raise Exception("underflow")
		else:
			self.top -= 1
			return self.S.pop()

	def print(self):
		print('stack: ', self.S)
