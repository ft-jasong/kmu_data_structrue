from stacks import Stack

class Infix:
	def __init__(self, expr):
		(*self.expr,) = expr
	def translate_postfix(self):
		stack = Stack(len(self.expr))
		list_ = []
		*ops, = "+-*/"
		for token in self.expr:
			if token in ops:
				if not stack.is_empty() and stack.peek() in ops:
					list_.append(stack.peek())
					stack.pop()
				stack.push(token)
			elif token == '(':
				stack.push(token)
			elif token == ')':
				while stack.peek() != '(':
					list_.append(stack.peek())
					stack.pop()
				stack.pop()
			else:
				list_.append(token)
				
		while not stack.is_empty():
			list_.append(stack.peek())
			stack.pop()
		return "".join(list_)
