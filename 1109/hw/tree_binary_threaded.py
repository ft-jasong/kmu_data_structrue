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
				stack.push(TreeNodeThreaded(token))
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

class TreeNodeThreaded:
	def __init__(self, elem=None):
		self.elem = elem
		self.left_child = self.right_child = None
		self.left_thread = self.right_thread = False
	def __repr__(self):
		return str(self)
	def __str__(self):
		return f"{self.elem}"

class ThreadedBinaryTree:
	"""Threaded Binary Tree"""
	def __init__(self, root=None):
		self.root = root
		self.head = TreeNodeThreaded()
		self.head.left_thread = True
		self.head.right_thread = False
		self.head.left_child = self.head
		self.head.right_child = self.head
		self.__build()
	def __build(self):
		"""using inorder traversal"""
		root = self.root
		actions = []

		if root is None:
			return
		def thread_recursive(root):
			if root is None:
				return
			thread_recursive(root.left_child)
			actions.append(root)
			thread_recursive(root.right_child)
		thread_recursive(root)

		actions[0].left_child = root
		actions[-1].right_child = self.head
		self.right_child = self.head
		for i in range(len(actions)):
			if actions[i].left_child is None:
				actions[i].left_thread = True
				if i != 0:
					actions[i].left_child = actions[i - 1]
			if actions[i].right_child is None:
				actions[i].right_thread = True
				if i != len(actions) - 1:
					actions[i].right_child = actions[i + 1]

	def find_successor(self, root):
		node = None
		if root is None:
			raise Exception("root node is None")
		def find_recursive(f_root):
			nonlocal node
			if f_root is None:
				return
			find_recursive(f_root.left_child)
			if root == f_root:
				node = f_root.right_thread
			find_recursive(f_root.right_child)
		print(node)
		return node

	def traverse_inorder(self):
		root = self.find_successor(self.head)
		ret = []
		while root is not None and root is not self.head:
			ret.append(root)
			root = self.find_successor(root)
		return ret

if __name__ == "__main__":
	sexpr = "( A ( B ( D ( H I ) E ) C ( F G ) ) )".split()
	root_ = BTreeBuilder.build(sexpr)
	tree = ThreadedBinaryTree(root_)
	root = tree.root
	e = root.left_child.right_child
	print(f"{e.left_child} <{e}> {e.right_child}")
	f = root.right_child.left_child
	print(f"{f.left_child} <{f}> {f.right_child}")
	g = root.right_child.right_child
	print(f"{g.left_child} <{g}> {g.right_child}")
	h = root.left_child.left_child.left_child
	print(f"{h.left_child} <{h}> {h.right_child}")
	i = root.left_child.left_child.right_child
	print(f"{i.left_child} <{i}> {i.right_child}")
	print()
	actions = tree.traverse_inorder()
	print(actions)