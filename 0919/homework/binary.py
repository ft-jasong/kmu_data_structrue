class Binary:
	def __init__(self, _bin):
		self.bin = _bin
	def __len__(self):
		return len(self.bin)
	def __str__(self):
		return ''.join(str(e) for e in self.bin)
	def __add__(self, other):
		if not isinstance(other, Binary):
			raise Exception("should not be different type")
		add_ = []
		for 
		add_.append()
		return Binary(add_)
	def __getitem__(self, id):
		return self.bin[id]

*data, = "110101011"
*data, = map(int, data)
b1 = Binary(data)
print(b1) # 110101011
print(len(b1)) # 9

*data, = "110111"
*data, = map(int, data)
b2 = Binary(data)
print(b2) # 110111
print(len(b2)) # 6

# b = b1 + b2
# print(b) # 111100010
# print(len(b)) # 9
# print(b[4]) # 0