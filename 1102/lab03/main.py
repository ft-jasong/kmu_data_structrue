from btree_builder import BTreeBuilder
from btree import BTree

sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
root = BTreeBuilder.build(sexpr)
tree = BTree(root)
actions = tree.traverse_postorder()
print(actions)