class Element:
	def __init__(self, value=0): # default argument(parameter)
		self.value = value
	def __str__(self):
		return f"Element: {self.value}"

elem = Element()
print(elem)
elem = Element(10)
print(elem)
