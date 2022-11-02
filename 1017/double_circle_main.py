from circular_doubly_linked_list import *

list_ = CircularDoublyLinkedList()
list_.add_tail(Node(10))
list_.add_tail(Node(20))
print(1, list_)
list_.add_head(Node(30))
print(4, list_)
for i in list_:
	print("Element:", i)
print()
it = iter(list_)
while True:
	try:
		i = next(it)
	except StopIteration:
		break
	print("Element:", i)
print(5, list_)
while not list_.is_empty():
	list_.delete_tail()
	print(6, list_)
list_.add_tail(Node(20))
print(7, list_)
list_.add_head(Node(30))
print(8, list_)
list_.insert_after(Node(30), Node(40))
print(9, list_)
list_.insert_before(Node(20), Node(10))
print(10, list_)
list_.delete(Node(40))
print(11, list_)
list_.delete(Node(30))
print(12, list_)
list_.delete(Node(20))
print(13, list_)