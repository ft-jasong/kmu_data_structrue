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