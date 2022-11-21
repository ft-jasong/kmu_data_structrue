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
	
	def search_dfs(self, elem):
		ret = None
		def dfs_recursive(root):
			nonlocal ret

			if root is None:
				return
			dfs_recursive(root.left_child)
			dfs_recursive(root.right_child)
			if root.elem == elem:
				ret = root
				return ret
		dfs_recursive(self.root)
		return ret