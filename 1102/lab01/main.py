from btree_builder import BTreeBuilder
from btree import BTree

# sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
# quiz
sexpr = "( A ( B ( D ( G H ) # ) C ( E ( # I ) F ) )"
root = BTreeBuilder.build(sexpr)
tree = BTree(root)
actions = tree.traverse_inorder()
print(actions)