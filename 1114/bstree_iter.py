from btree_builder import BTreeBuilder

class BSTree:
	def __init__(self, root):
		self.root = root

	def search(self, elem):
		if self.root is None:
			raise Exception("the root is none")
		cur = self.root
		while cur is not None and cur.elem != elem:
			# if elem > cur.elem:
			# 	cur = cur.right_child
			# elif elem < cur.elem:
			# 	cur = cur.left_child
			cur = cur.left_child if elem < cur.elem else cur.right_child
		return cur

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