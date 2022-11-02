class Node:
	
	def __init__(self, item=None):
		self.item = item
		self.llink = self.rlink = None

	def __eq__(self, other):
		if not isinstance(other, Node):
			return False
		if self is other or self.item == other.item:
			return True
		return False

	def __str__(self):
		return f"{self.item}"

	def __repr__(self):
		return str(self)

class CircularDoublyLinkedList:
	"""class Doubly linked list"""
	def __init__(self):
		self.head = None

	def add_head(self, node_new: Node):
		if self.head is None:
			self.head = node_new
			self.head.rlink = self.head
			self.head.llink = self.head
		else:
			tail = self.head.llink
			self.head.llink = node_new
			tail.rlink = node_new
			node_new.llink = tail
			node_new.rlink = self.head
			self.head = node_new

	def add_tail(self, node_new: Node):
		if self.head is None:
			self.head = node_new
			self.head.rlink = self.head
			self.head.llink = self.head
		else:
			cur_tail = self.head.llink
			node_new.llink = cur_tail
			node_new.rlink = self.head
			cur_tail.rlink = node_new
			self.head.llink = node_new

	def delete_head(self):
		if self.is_empty():
			raise Exception("list is empty.")
		if self.head.llink == self.head:
			self.head = None
		else:
			new_head = self.head.rlink
			tail = self.head.llink
			new_head.llink = self.head.llink
			tail.rlink = new_head
			self.head = new_head

	def delete_tail(self):
		if self.is_empty():
			raise Exception("list is empty.")
		if self.head.llink == self.head:
			self.head = None
		else:
			new_tail = self.head.llink.llink
			new_tail.rlink = self.head
			self.head.llink = new_tail
			
	def insert_before(self, node: Node, node_new: Node):
		if self.is_empty():
			raise Exception("list is empty.")
		cur = self.head
		while cur.rlink != self.head and cur != node:
			cur = cur.rlink
		if cur == node:
			prev_node = cur.llink
			node_new.llink = prev_node
			node_new.rlink = cur
			prev_node.rlink = node_new
			cur.llink = node_new
		else:
			raise Exception(f"cannot find {node}")
	def insert_after(self, node: Node, node_new: Node):
		if self.is_empty():
			raise Exception("list is empty.")
		cur = self.head
		while cur.rlink != self.head and cur != node:
			cur = cur.rlink
		if cur == node:
			next_node = cur.rlink
			node_new.llink = cur
			node_new.rlink = next_node
			cur.rlink = node_new
			next_node.llink = node_new
		else:
			raise Exception(f"cannot find {node}")
	def delete(self, node):
		if self.is_empty():
			raise Exception("list is empty.")
		cur = self.head
		while cur.rlink != self.head and cur != node:
			cur = cur.rlink
		if node == self.head:
			self.delete_head()
		elif cur == node:
			cur.llink.rlink = cur.rlink
			cur.rlink.llink = cur.llink
		else:
			raise Exception(f"cannot find {node}")
	def __iter__(self):
		self.next_ = self.head
		return self

	def __next__(self):
		if self.next_ is None:
			raise StopIteration
		if self.next_.rlink == self.head:
			n = self.next_
			self.next_ = None
			return f"{n}"
		n = self.next_
		self.next_ = self.next_.rlink
		return f"{n}"
		
	def is_empty(self):
		if self.head is None:
			return True
		return False
	def __str__(self):
		ret = []
		if self.head is None:
			return f"{ret}"
		cur = self.head
		while cur.rlink != self.head:
			ret.append(str(cur))
			cur = cur.rlink
		if cur.rlink == self.head:
			ret.append(str(cur))
		return f"{ret}"

class Stack:
	def __init__(self):
		self.list_ = CircularDoublyLinkedList()
	def push(self, elem):
		self.list_.add_head(Node(elem))
	def pop(self):
		self.list_.delete_head()
	def peek(self):
		return f"self.list_.head"
	def is_empty(self):
		return self.list_.is_empty()
	def __iter__(self):
		return iter(self.list_)
	def __str__(self):
		return str(self.list_)
