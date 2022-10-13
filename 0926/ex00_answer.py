class OrderedList:
	def __init__(self):
		self.elems = []

	def __len__(self):
		return len(self.elems)

	def __getitem__(self, index):
		return self.elems[index]
	
	def __str__(self):
		return str(self.elems)

	def is_empty(self):
		return not bool(self.elems)

	def add(self, elem):
		if not self.elems:
			self.elems.append(elem)
			return
		cur = 0
		while cur < len(self) and self[cur] <= elem:
			cur += 1
		self.elems.insert(cur, elem)

	def remove(self, elem):
		self.elems.remove(elem)

	def search(self, elem):
		cur = 0
		while cur < len(self) and self[cur] != elem:
			cur += 1
		return False if cur >= len(self) else True
	
	def index(self, item):
		for i, n in enumerate(self.elems):
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