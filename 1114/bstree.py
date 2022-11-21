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

class BSTree:
	def __init__(self, root):
		self.root = root

	def traverse_preorder(self):
		ret = []
		def preorder_recursive(root):
			if root is None:
				return
			ret.append(root)
			preorder_recursive(root.left_child)
			preorder_recursive(root.right_child)
		preorder_recursive(self.root)
		return ret

	def delete(self, elem):
		parent = None
		root = self.root

		while root is not None and elem != root.elem:
			parent = root
			root = root.left_child if elem < root.elem else root.right_child
		if root is None:
			return
		
		minmax = root
		while minmax.right_child is not None:
			minmax = minmax.right_child
		if minmax == root:
			if parent.left_child == root:
				parent.left_child = None
			else:
				parent.right_child = None
		else:
			root.elem = minmax.elem
		if minmax.left_child is not None:
			minmax.elem = minmax.left_child.elem
			minmax.left_child = None

sexpr = "( 30 ( 5 ( 2 # ) 40 ) )".split()
sexpr = [int(i) if i.isnumeric() else i for i in sexpr]
root = BTreeBuilder.build(sexpr)
tree = BSTree(root)
actions = tree.traverse_preorder()
print(actions)
tree.delete(40)