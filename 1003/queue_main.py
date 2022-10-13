from queues import Queue

# if __name__ == "__main__":
# 	N = 5
# 	q = Queue(N)
# 	print("Length:", len(q))
# 	print("Empty:", q.is_empty())
# 	print("Enqueue 1-", N)
# 	for i in range(1, N + 1):
# 		q.enqueue(i)
# 		print("Peeking:", q.peek())
# 		print("Queue =", q)
# 		print("Length:", len(q))
# 	print("Empty:", q.is_empty())
# 	while not q.is_empty():
# 		print("Peeking:", q.peek())
# 		q.dequeue()
# 		print("Queue =", q)
# 		print("Length:", len(q))
# 	print("Empty:", q.is_empty())

if __name__ == "__main__":
	N = 4
	queue = Queue(N)
	print(queue.is_empty())
	queue.enqueue(1)
	queue.enqueue(2)
	queue.enqueue(3)
	queue.dequeue()
	queue.dequeue()
	print(len(queue), queue)
	queue.enqueue(4)
	print(len(queue), queue)