class Node:
	def __init__(self, item=None):
		self.item = item
		self.next = None
	def __eq__(self, other):
		if not isinstance(other, Node):
			return False
		if self is other or self.item == other.item:
			return True
		return False
	def __str__(self):
		return f"{self.item}"
class CircularSinglyLinkedList:
	def __init__(self):
		self.tail= None
	def add_head(self, node_new):
		if self.tail is None:
			self.tail = node_new
			self.tail.next = self.tail
		elif self.tail == self.tail.next:
			self.tail.next = node_new
			node_new.next = self.tail
		else:
			node_new.next = self.tail.next
			self.tail.next = node_new
	def add_tail(self, node_new):
		if self.tail is None:
			self.add_head(node_new)
		else:
			node_new.next = self.tail.next
			self.tail.next = node_new
			self.tail = node_new
	def delete(self, node):
		if self.tail is None:
			raise Exception("linked list is empty")
		head = self.tail.next
		if self.tail == node:
			self.delete_tail()
			return
		elif head == node:
			self.delete_head()
			return
		while head != node and head != self.tail:
			prev = head
			head = head.next
		if head == self.tail:
			raise Exception(f"cannot find {node}")
		prev.next = head.next
	def delete_tail(self):
		if self.tail is None:
			raise Exception("No nodes in linked list")
		elif self.tail == self.tail.next:
			self.tail = None
		else:
			head = self.tail.next
			cur = head
			while cur.next != self.tail:
				cur = cur.next
			self.tail = cur
			cur.next = head
	def delete_head(self):
		if self.tail is None:
			raise Exception("No nodes in linked list")
		elif self.tail.next == self.tail:
			self.tail = None
		else:
			new_head = self.tail.next.next
			self.tail.next = new_head
	def insert_after(self, node, node_new):
		if self.tail is None:
			raise Exception("linked list is empty")
		if node == self.tail:
			self.add_tail(node_new)
			return
		cur = self.tail.next
		while cur != node and cur != self.tail:
			cur = cur.next
		if cur == self.tail:
			raise Exception(f"cannot find {node}")
		node_new.next = cur.next
		cur.next = node_new
	def insert_before(self, node, node_new):
		if self.tail is None:
			raise Exception("linked list is empty")
		if self.tail.next == node:
			self.add_head(node_new)
		elif self.tail == node:
			cur = self.tail.next
			while cur.next != self.tail:
				cur = cur.next
			cur.next = node_new
			node_new.next = self.tail
		else:
			cur = self.tail.next
			prev = None
			while cur != self.tail and cur != node:
				prev = cur
				cur = cur.next
			if cur == self.tail:
				raise Exception(f"cannot find {node}")
			prev.next = node_new
			node_new.next = cur
	def __str__(self):
		ret = []
		if self.tail is None:
			return f"{ret}"
		cur = self.tail.next
		while cur != self.tail:
			ret.append(str(cur))
			cur = cur.next
		if self.tail is not None:
			ret.append(str(self.tail))
		return f"{ret}"

list_ = CircularSinglyLinkedList()
list_.add_head(Node(50))
list_.add_tail(Node(100))
list_.add_tail(Node(150))
print("1", list_)
list_.delete_head()
print("2", list_)
list_.delete_tail()
print("3", list_)
list_.delete_head()
print("4", list_)
list_.add_tail(Node(150))
list_.insert_before(Node(150), Node(999))
print("5", list_)
list_.add_head(Node(50))
list_.add_tail(Node(100))
print("6", list_)
list_.add_tail(Node(700))
print("7", list_)
list_.insert_after(Node(50), Node(250))
print("8", list_)
list_.insert_before(Node(50), Node(750))
list_.delete(Node(700))
print("9", list_)