from stack import Stack

class BTree:
	def __init__(self, root):
		self.root = root

	def traverse_inorder_iterative(self):
		#LVR
		ret = []
		root = self.root
		stack = Stack()
		while not stack.is_empty() or root is not None:
			while root is not None:
				stack.push(root)
				root = root.left_child
			
			node = stack.peek()
			stack.pop()
			ret.append(node)

			root = node.right_child

		return ret