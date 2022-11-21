from btree_builder import BTreeBuilder
from tree_node import TreeNode
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

	def search(self, elem):
		if self.root is None:
			raise Exception("the root is none")
		cur = self.root
		while cur is not None and cur.elem != elem:
			if elem > cur.elem:
				cur = cur.right_child
			elif elem < cur.elem:
				cur = cur.left_child
		return cur
	
	def insert(self, elem):
		parent = None
		root = self.root

		while root is not None and elem != root.elem:
			parent = root
			root = root.left_child if elem < root.elem else root.right_child

			if root is not None:
				return
			node_new = TreeNode(elem)
			if parent is None:
				self.root = node_new
				return

			if parent.elem > node_new.elem:
				parent.left_child = node_new
			else:
				parent.right_child = node_new


if __name__ == "__main__":
	sexpr = "( 30 ( 5 ( 2 # ) 40 ) )".split()
	sexpr = [int(i) if i.isnumeric() else i for i in sexpr]
	root = BTreeBuilder.build(sexpr)
	tree = BSTree(root)
	actions = tree.traverse_preorder()
	print(actions)
	tree.insert(40)
	actions = tree.traverse_preorder()
	print(actions)
	tree.insert(80)
	actions = tree.traverse_preorder()
	print(actions)
	found = tree.search(40)
	print(found.right_child)
	print(found.left_child)