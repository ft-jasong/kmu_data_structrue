class BTree:
	def __init__(self, root):
		self.root = root

	def traverse_preorder(self):
		ret = []
		# using recursive

		def preorder_recursive(root):
			if root is None:
				return
			ret.append(root)
			preorder_recursive(root.left_child)
			preorder_recursive(root.right_child)
		preorder_recursive(self.root)
		return ret