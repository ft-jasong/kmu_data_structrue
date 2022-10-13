class Term:
	def __init__(self, row=0, col=0, value=0):
		self.row = row
		self.col = col
		self.value = value

	def __str__(self):
		return f"{self.row, self.col, self.value}"

	def __repr__(self):
		return str(self)

def transpose_mat(mat):
	rows = len(mat)
	cols = len(mat[0])
	ret_mat = [[0] * rows for _ in range(cols)]

	for row in range(rows):
		for col in range(cols):
			ret_mat[col][row] = mat[row][col]
	return ret_mat
	# for row in range(len(mat)):
	# 	for col in range(len(mat[0])):
	# 		if row < col:
	# 			tmp = mat[row][col]
	# 			mat[row][col] = mat[col][row]
	# 			mat[col][row] = tmp

def transpose(self):
	if self.sparse is None:
		return
	
	sparse = [Term() for _ in range(self.size)]
	idx = 0
	for i in range(self.cols):
		for e in self.sparse:
			if e.col != i:
				continue
			sparse[idx].row = e.col
			sparse[idx].col = e.row
			sparse[idx].value = e.value
			idx += 1
		return MatrixSparse (
			rows=self.rows,
			cols=self.cols,
			size=self.size,
			sparse=self.sparse
		)


data = [
	[15, 0, 0, 22, 0, -15],
	[0, 11, 3, 0, 0, 0],
	[0, 0, 0, -6, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[91, 0, 0, 0, 0, 0],
	[0, 0, 28, 0, 0, 0],
]
print(data)
print("transpose matrix >>")
transpose_mat(data)
print(data)
