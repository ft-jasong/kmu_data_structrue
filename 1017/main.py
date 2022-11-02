from stack import Stack

stack = Stack()
stack.push(10)
stack.push(20)
print(stack)
print("peek:", stack.peek())
stack.pop()
print(stack)
stack.push(30)
print(stack)
stack.push(40)
print(stack)
print("peek:", stack.peek())
stack.pop()
print(stack)
for i in stack:
	print("Element:", i)
print()
print(stack)
while not stack.is_empty():
	print("peek:", stack.peek())
	stack.pop()
	print(stack)
