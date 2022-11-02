class Node:
	def __init__(self, item=None):
		self.item = item
		self.rlink = self.llink = None
	
	def __eq__(self, other):
		if not isinstance(other, Node):
			return False
		if self is other or self.item == other.item:
			return True
		return False
	
	def __str__(self):
		return f"{self.item}"


class DoublyLinkedList:
	def __init__(self):
		self.tail= None
	
	def add_head(self, node_new):
		if self.tail is None:
			self.tail = node_new
		else:
			cur = self.tail
			while cur.llink is not None:
				cur = cur.llink
			node_new.rlink = cur
			cur.llink = node_new
	
	def add_tail(self, node_new):
		if self.tail is None:
			self.tail = node_new
		else:
			self.tail.rlink = node_new
			node_new.llink = self.tail
			self.tail = node_new
	
	def delete_tail(self):
		if self.tail is None:
			raise Exception("no elements in doubly linked list")
		elif self.tail.llink is None:
			self.tail = None
		else:
			self.tail = self.tail.llink
			self.tail.rlink = None
	
	def delete_head(self):
		cur = self.tail
		if cur is None:
			raise Exception("no elements in doubly linked list")
		elif cur.llink is None:
			self.tail = None
		else:
			new_head = None
			while cur.llink is not None:
				new_head = cur
				cur = cur.llink
			if new_head is not None:
				new_head.llink = None
	
	def delete (self, node):
		if self.tail is None:
			raise Exception("no elements in doubly linked list")
		elif self.tail == node:
			self.delete_tail()
		else:
			cur = self.tail
			while cur != node and cur is not None:
				cur = cur.llink
			if cur is None:
				raise Exception(f"cannot find {node}")
			elif cur.llink is None:
				self.delete_head()
			else:
				prev_node = cur.llink
				prev_node.rlink = cur.rlink
				cur.rlink.llink = prev_node
	
	def insert_after(self, node, node_new):
		cur = self.tail
		if cur is None:
			raise Exception("no elements in doubly linked list")
		else:
			while cur is not None and cur != node:
				cur = cur.llink
			if cur is None:
				raise Exception(f"cannot find {node}")
			else:
				next_node = cur.rlink
				node_new.llink = cur
				node_new.rlink = cur.rlink
				cur.rlink = node_new
				next_node.llink = node_new

	def insert_before(self, node, node_new):
		cur = self.tail
		if cur is None:
			raise Exception(f"cannot find {node}")
		else:
			while cur is not None and cur != node:
				cur = cur.llink
			if cur is None:
				raise Exception(f"cannot find {node}")
			elif cur.llink is None:
				self.add_head(node_new)
			else:
				prev_node = cur.llink
				prev_node.rlink = node_new
				node_new.llink = prev_node
				node_new.rlink = cur
				cur.llink = node_new
	
	def __str__(self):
		ret = []
		cur = self.tail
		while cur is not None:
			ret.append(str(cur))
			cur = cur.llink
		return f"{ret[::-1]}"


list_ = DoublyLinkedList()
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
print("4-1", list_)
list_.delete(Node(150))
list_.add_head(Node(50))
print("4-2", list_)
list_.delete_head()
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
# while True: # exception
# 	list_.delete_head()
# for i in range(10): #exception
# 	print(i)
# 	list_.delete_tail()

