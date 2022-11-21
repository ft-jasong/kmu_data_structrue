class BTree:
	def __init__(self, root):
		self.root = root

	def traverse_postorder(self):
		ret = []
		# using recursive

		def postorder_recursive(root):
			if root is None:
				return
			postorder_recursive(root.left_child)
			postorder_recursive(root.right_child)
			ret.append(root)
		postorder_recursive(self.root)
		return ret