from stack import Stack

class Tree:
	def __init__(self):
		self.root = None
	def build(self, sexpr):
		stack = Stack()
		for e in sexpr:
			if e == ')':
				while stack.peek() != '(':

			else:
				stack.push(e)
		
class TreeNode:
	def __init__(self, elem):
		self.elem = elem
		self.left_child = None
		self.right_sibling = None
	def __repr__(self):
		return str(self)
	def __str__(self):
		return f"{self.elem}"