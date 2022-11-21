from queues import Queue

class BTree:
	def __init__(self, root):
		self.root = root

	def search_bfs(self, elem):
		#iterator
		ret = None

		queue = Queue()
		queue.enqueue(self.root)
		while not queue.is_empty():
			top = queue.peek()
			if top.elem == elem:
				ret = top.elem
				break
			if top.left_child is not None:
				queue.enqueue(top.left_child)
			if top.right_child is not None:
				queue.enqueue(top.right_child)
			queue.dequeue()
		return ret