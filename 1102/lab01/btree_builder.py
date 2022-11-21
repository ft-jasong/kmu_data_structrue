from stack import Stack
from tree_node import TreeNode

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