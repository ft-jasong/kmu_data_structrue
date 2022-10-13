from queues_circular import Queue

if __name__ == "__main__":
	N = 8
	queue = Queue(N)
	queue.enqueue("A")
	queue.enqueue("B")
	queue.enqueue("C")
	queue.enqueue("D")
	print(queue)
	print("Peek:", queue.peek())
	queue.dequeue()
	print("Peek:", queue.peek())
	queue.dequeue()
	print(queue)
	queue.enqueue("E")
	queue.enqueue("F")
	queue.enqueue("G")
	queue.enqueue("H")
	queue.enqueue("I")
	queue.enqueue("J")
	print(queue)
	queue.dequeue()
	print(queue)
	for i in queue:
		print("Element:", i)
	print("Peek:", queue.peek())
	while not queue.is_empty():
		queue.dequeue()
	print(queue)