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