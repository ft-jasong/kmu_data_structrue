class OrderedList:
	def __init__(self):
		self._list = []
	def __str__(self):
		return f"{self._list}"
	def add(self, item):
		if self.is_empty():
			self._list.insert(0, item)
		for i, n in enumerate(self._list):
			if item < n:
				self._list.insert(i, item)
				break
	def is_empty(self):
		if len(self._list) > 0:
			return False
		return True
	def remove(self, item):
		self._list.remove(item)
	def search(self, item):
		for n in self._list:
			if n > item:
				return False
			elif n == item:
				return True
	def size(self):
		return len(self._list)
	def index(self, item):
		for i, n in enumerate(self._list):
			if n > item:
				return None
			elif n == item:
				return i


*data, = 53, 17, 34, 23, 15, 43
print(data)
o = OrderedList()
print(o.is_empty())
for i in data:
	o.add(i)
print(o.is_empty())
print(o)
o.remove(23)
print(o)
print(o.search(43))
print(o.index(23))