from singly_linkedlist import *

class Stack:
	def __init__(self):
		self.list_ = SinglyLinkedList()
	def push(self, elem):
		self.list_.add_head(Node(elem))
	def pop(self):
		if self.is_empty():
			raise Exception("stack is empty")
		self.list_.delete_head()
	def peek(self):
		if self.is_empty():
			raise Exception("stack is empty")
		elem = str(self.list_.head)
		return elem
	def is_empty(self):
		return 
	def __iter__(self):
		# return self.list_
		return iter(self.list_)
	def __str__(self):
		return f"{self.list_}"