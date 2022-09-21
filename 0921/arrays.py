class Array:
	def __init__(self, length_ = 10):
		self.arr = [0] * length_
	def __str__(self):
		return (f"{self.arr}")
	def __getitem__(self, id):
		return self.arr[id]
	def __setitem__(self, id, num):
		self.arr[id] = num
	def __len__(self):
		return (len(self.arr))
	
if __name__ == "__main__":
	arr = Array(5)

	for i in range(len(arr)):
		arr[i] = i
	
	print(arr)
	index = 3
	print(f"arr[{index}] = {arr[index]}")

	for i in arr:
		print(id(i), i)
	print(sum(arr))