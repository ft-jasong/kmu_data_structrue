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
		self.value = None # boolean value
		self.left_child = self.right_child = None
	def __repr__(self):
		return str(self)
	def __str__(self):
		return f"{self.elem}"
		

class PropositionalTree:
	def __init__(self, root):
		self.root = root

	def calculate_propositional(self, *param):
		ret = None
		def calculate_recursive(root):
			nonlocal ret
			if root is None:
				return None
			if str.isdigit(root.elem) is True:
				root.value = param[int(root.elem)]
				return root.value
			else:
				l_value = calculate_recursive(root.left_child)
				r_value = calculate_recursive(root.right_child)
				if root.elem == "AND":
					root.value = l_value and r_value
				elif root.elem == "OR":
					root.value = l_value or r_value
				else:
					if l_value is not None and r_value is None:
						root.value = not l_value
					else:
						root.value = not r_value
				ret = root
				return root.value
		calculate_recursive(self.root)
		return ret

class BTreeBuilder:
	@staticmethod
	def build(sexpr):
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
		return root


sexpr = "( OR ( OR ( AND ( 0 NOT ( # 1 ) ) AND ( NOT ( # 0 ) 2 ) ) NOT ( # 2 ) ) )".split()
root = BTreeBuilder.build(sexpr)
tree = PropositionalTree(root)
prop = tree.calculate_propositional(False, True, False)
print(prop.value)