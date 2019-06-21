#************************************************
# Queue class
# Note: FIFO property
#************************************************

class Queue():
	def __init__(self, length):
		self.length = length
		self.head = 0
		self.tail = 0
		self.Q = []
		for i in range(length):
			self.Q = self.Q + [-1]

	def enqueue(self, x):
		self.Q[self.tail] = x
		if self.tail == self.length:
			self.tail = 1
		else:
			self.tail += 1

	def dequeue(self):
		x = self.Q[self.head]
		self.Q[self.head] = -1
		if self.head == self.length:
			self.head = 1
		else:
			self.head += 1
		return x
