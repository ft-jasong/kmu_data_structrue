class BTree:
	def __init__(self, root):
		self.root = root

	def traverse_inorder(self):
		ret = []
		# using recursive

		def inorder_recursive(root):
			if root is None:
				return
			inorder_recursive(root.left_child)
			ret.append(root)
			inorder_recursive(root.right_child)
		inorder_recursive(self.root)
		return ret