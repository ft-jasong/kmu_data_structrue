class Stack:
	def __init__(self):
		self.items = []
	def is_empty(self):
		return not self.items
	def push(self, elem):
		self.items.append(elem)
	def pop(self):
		if self.is_empty():
			raise Exception("stack is empty.")
		self.items.pop()
	def peek(self):
		if self.is_empty():
			raise Exception("stack is empty.")
		return self.items[-1]
	def __iter__(self):
		pos = 0
		while pos < len(self):
			yield self.items[pos]
			pos += 1
	def __len__(self):
		return len(self.items)
	def __str__(self):
		return str(self.items)

class TreeNode:
	def __init__(self, elem):
		self.elem = elem
		self.left_child = None
		self.right_child = None
	def __repr__(self):
		return str(self)
	def __str__(self):
		return f"{self.elem}"

class BTree:
	def __init__(self):
		self.root = None
	
	def build(self, sexpr):
		stack = Stack()
		it = iter(sexpr)
		root = None
		while stack.is_empty() or it:
			try:
				token = next(it)	
			except StopIteration:
				break
			if token != ")":
				if token == "#":
					token = None
				stack.push(TreeNode(token))
				continue
			l_child = None
			r_child = None
			if not stack.is_empty():
				r_child = stack.peek()
				stack.pop()
			if not stack.is_empty():
				l_child = stack.peek()
				stack.pop()
			if not stack.is_empty() and stack.peek().elem == "(":
				stack.pop()
			if not stack.is_empty():
				root = stack.peek()
				stack.pop()
			else:
				root = r_child
				break
	
			if l_child.elem != None:
				root.left_child = l_child
			else:
				root.left_child = None
			if r_child.elem != None:
				root.right_child = r_child
			else:
				root.right_child = None
			stack.push(root)
		if not stack.is_empty():
			raise Exception("expression is wrong.")
		self.root = root

if __name__ == "__main__":
	sexpr = "( 30 ( 5 ( 2 # ) 40 ( # 80 ) ) )".split()
	tree = BTree ()
	tree.build(sexpr)
	root = tree.root
	print(root)
	print(root.left_child)
	print(root.left_child.left_child)
	print(root.left_child.right_child)
	print(root.right_child)
	print(root.right_child.left_child)
	print(root.right_child.right_child)