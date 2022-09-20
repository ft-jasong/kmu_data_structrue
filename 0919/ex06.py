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
	def __sub__(self, other):
		if not isinstance(other, Element):
			raise Exception("should not be different type.")
		sub_ = self.value - other.value
		return Element(sub_)

class Elements:
	def __init__(self, cap=10):
		self.cap = cap
		self.elems = [None] * cap
	def __setitem__(self, id, elem):
		self.elems[id] = elem
	def __getitem__(self, id):
		return self.elems[id]
	def __str__(self):
		return f"{self.elems}"

elems = Elements()
elems[0] = Element(10)
elems[1] = Element(20)

print(elems)