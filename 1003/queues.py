from shutil import ExecError


class Array:
	CAPACITY = 10

	def __init__(self, capacity=CAPACITY):
		self.items = [None] * capacity
	
	def __len__(self):
		return len(self.items)
	
	def __getitem__(self, index):
		return self.items[index]
	
	def __setitem__(self, index, item):
		self.items[index] = item
	
	def __str__(self):
		return f"{self.items}"
	
class Queue:
	CAPACITY = 10
	def __init__(self, capacity=CAPACITY):
		self.arr = Array(capacity)
		self.capacity = capacity
		self.front = self.rear = -1
	def __len__(self):
		return len(self.arr)
	def is_full(self):
		return self.front >= self.capacity
	def is_empty(self):
		return self.rear == -1
	def enqueue(self, elem):
		if self.is_full():
			raise Exception("Queue is full")
		self.rear += 1
		self.arr[self.rear] = elem

		if self.front < 0:
			self.front = 0
	def dequeue(self):
		if self.is_empty():
			raise Exception("Queue is empty")
		self.arr[self.front] = None
		if self.front == self.rear and self.front != -1:
			self.front  = self.rear = -1
		else: self.front += 1
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
		while pos <= self.rear:
			yield self.arr[pos]
			pos += 1
	def __str__(self):
		return str(self.arr)