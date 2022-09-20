class Element:
	def __init__(self, value=0): # default argument(parameter)
		self.value = value
	def __str__(self):
		return f"Element: {self.value}"
	def __repr__(self): # representation
		return str(self)
	def __add__(self, other): # 이것도 Cpp operator+ overloading과 비슷함.
		if not isinstance(other, Element):
			raise Exception("should not be different type.")
		add_ = self.value + other.value
		return Element(add_)

res = Element(10) + Element(10)
print(res)