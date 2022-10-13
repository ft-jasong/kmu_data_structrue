from arrays import Array
	
class Queue:
	CAPACITY = 10
	def __init__(self, capacity=CAPACITY):
		self.arr = Array(capacity)
		self.capacity = capacity
		self.front = self.rear = -1
	def __len__(self):
		if self.is_empty():
			return 0
		if self.rear < self.front:
			return self.capacity - self.front + self.rear + 1
		return self.rear - self.front + 1
	def is_full(self):
		return self.front == (self.rear + 1) % self.capacity
	def is_empty(self):
		return self.front == -1 and self.rear == -1
	def enqueue(self, elem):
		if self.is_full():
			raise Exception("queue is full.")
		self.rear = (self.rear + 1 ) % self.capacity
		self.arr[self.rear] = elem
		if self.front < 0:
			self.front += 1
	def dequeue(self):
		if self.is_empty():
			raise Exception("queue is empty.")
		
		self.arr[self.front] = None
		if self.front == self.rear:
			self.front = self.rear = -1
			return
		self.front = (self.front + 1) % self.capacity
	def peek(self):
		if self.is_empty():
			raise Exception("Queue is empty")
		return self.arr[self.front]
	def __len__(self):
		if self.is_empty():
			return 0
		if self.rear < self.front:
			return self.capacity - self.front + self.rear + 1
		return self.rear - self.front + 1
	def __iter__(self):
		if self.is_empty():
			return
		pos = self.front
		while pos < self.rear:
			yield self.arr[pos % self.capacity]
			pos += 1
	def __str__(self):
		return str(self.arr)