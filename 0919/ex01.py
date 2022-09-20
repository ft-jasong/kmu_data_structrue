class Element:
	def __init__(self, value=0): # default argument(parameter)
		self.value = value
	def __str__(self):
		return f"Element: {self.value}"
	def __repr__(self): # representation
		return str(self)

elems = [Element(100), Element(200)]
print(elems)