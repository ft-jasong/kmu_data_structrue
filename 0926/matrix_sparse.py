class Term:
	def __init__(self, row=0, col=0, value=0):
		self.row = row
		self.col = col
		self.value = value
	def __str__(self):
		return f"{self.row, self.col, self.value}"
	def __repr__(self):
		return str(self)

class MatrixSparse:
	def __init__(self, rows=0, cols=0, size=0, sparse=None):
		self.rows = rows
		self.cols = cols
		self.size = size
		self.sparse = sparse
	def build_matrix_sparse(self, mat):
		# if self.sparse is None:
		# 	self.sparse = []
		# for row in range(len(mat)):
		# 	for col in range(len(mat[0])):
		# 		if (mat[row][col] != 0):
		# 			self.sparse.append(Term(row, col, mat[row][col]))
		self.rows = len(mat)
		self.cols = len(mat[0])
		self.sparse = [
			Term(r, c, v)
			for r, row in enumerate(mat)
			for c, v in enumerate(row)
			if v != 0
		]
	def __str__(self):
		result = [str(item) for item in self.sparse]
		return .join(result) # 짱이시네욭

data = [
	[15, 0, 0, 22, 0, -15],
	[0, 11, 3, 0, 0, 0],
	[0, 0, 0, -6, 0, 0],
	[0, 0, 0, 0, 0, 0],
	[91, 0, 0, 0, 0, 0],
	[0, 0, 28, 0, 0, 0],
]
print("sparse matrix >>")
mat = MatrixSparse()
mat.build_matrix_sparse(data)
print(mat)