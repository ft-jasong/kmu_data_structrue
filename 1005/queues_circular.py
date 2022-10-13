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
		return self.rear == self.front + self.capacity - 1
	def is_empty(self):
		return self.front > self.rear
	def enqueue(self, elem):
		if self.is_full():
			raise Exception("queue is full.")
		if self.front == -1:
			self.front = 0
		self.rear += 1
		self.arr[self.rear % self.capacity] = elem
	def dequeue(self):
		if self.is_empty():
			raise Exception("queue is empty.")
		self.arr[self.front % self.capacity] = None
		self.front += 1
	def peek(self):
		if self.is_empty():
			raise Exception("Queue is empty")
		return self.arr[self.front]
	def __len__(self):
		return 0 if self.is_empty() else self.rear - self.front + 1
	def __iter__(self):
		if self.is_empty():
			return
		pos = self.front
		while pos < self.rear:
			yield self.arr[pos % self.capacity]
			pos += 1
	def __str__(self):
		return str(self.arr)