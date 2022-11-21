from btree_builder import BTreeBuilder

class BSTree:
	def __init__(self, root):
		self.root = root

	def search(self, elem):
		if self.root is None:
			raise Exception("the root is none")
		def search_recursive(root):
			nonlocal elem
			if root is None:
				return None
			if elem == root.elem:
				return root
			elif elem < root.elem:
				return search_recursive(root.left_child)
			else:
				return search_recursive(root.right_child)
		return search_recursive(self.root)

if __name__ == "__main__":
	sexpr = "( 30 ( 5 ( 2 # ) 40 ) )".split()
	sexpr = [int(i) if i.isnumeric() else i for i in sexpr]
	root = BTreeBuilder.build(sexpr)
	tree = BSTree(root)
	found = tree.search(5)
	print(found)
	found = tree.search(2)
	print(found)
	found = tree.search(40)
	print(found)
	found = tree.search(30)
	print(found)
	found = tree.search(35)
	print(found)