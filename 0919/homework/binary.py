class Binary:
	def __init__(self, _bin):
		self.bin = _bin
	def __len__(self):
		return len(self.bin)
	def __str__(self):
		return ''.join(str(e) for e in self.bin)
	def __getitem__(self, id):
		return self.bin[id]
	def __add__(self, other):
		if not isinstance(other, Binary):
			raise Exception("should not be different type")
		add_ = []
		carry = 0
		min_len = min(len(self), len(other))
		for i in range(1, min_len + 1):
			add_.insert(0, self[-i] ^ other[-i] ^ carry)
			carry = (self[-i] & carry) | (other[-i] & carry) | (self[-i] & other[-i])
		if min_len is len(self):
			for i in range(min_len + 1, len(other) + 1):
				add_.insert(0, other[-i] ^ carry)
				carry = other[-i] & carry
		else:
			for i in range(min_len + 1, len(self) + 1):
				add_.insert(0, self[-i] ^ carry)
				carry = self[-i] & carry
		if carry is 1:
			add_.insert(0, carry)
		return Binary(add_)


*data, = "110101011"
*data, = map(int, data)
b2 = Binary(data)
print(b2) # 110101011
print(len(b2)) # 9

*data, = "110111"
*data, = map(int, data)
b1 = Binary(data)
print(b1) # 110111
print(len(b1)) # 6

b = b1 + b2
print(b) # 111100010
print(len(b)) # 9
print(b[4]) # 0