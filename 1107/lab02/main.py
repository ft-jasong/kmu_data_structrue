from btree_builder import BTreeBuilder
from btree import BTree

sexpr = "( + ( * ( * ( / ( A B ) C ) D ) E ) )".split()
root = BTreeBuilder.build(sexpr)
tree = BTree(root)
for e in sexpr:
	found = tree.search_bfs(e)
	print("target:", e, " found:", found)