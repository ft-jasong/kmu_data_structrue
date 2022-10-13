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
	def __init__(self, rows=0, cols=0, size=0, sparse = None):
		self.rows = rows
		self.cols = cols
		self.size = size
		self.sparse = sparse

	def __str__(self):
		result = [str(item) for item in self.sparse]
		return "\n".join(result)

	def build_matrix_sparse(self, mat):
		self.rows = len(mat)
		self.cols = len(mat[0])

		self.sparse = [
			Term(r, c, v)
			for r, row in enumerate(mat) # row index
			for c, v in enumerate(row) # col index
			if v!= 0 # 0이 아닌 값만 row와 col, 그리고 해당 value를 Term에다가 저장. 그리고 그걸 Sparse에 list로 저장
		]
		self.size = len(self.sparse) # 결국 sparse 내부 Term의 개수.
	
	def transpose(self):
		if self.sparse is None: # sparse 자체가 아무것도 없다면 전치행렬이 존재할 수 없으니 그냥 return
			return
		sparse = [Term() for _ in range(self.size)] # size만큼의 sparse  

		idx = 0
		for i in range(self.cols):
			for e in self.sparse:
				if e.col != i:
					continue
				sparse[idx].row = e.col
				sparse[idx].col = e.row
				sparse[idx].value = e.value
				idx += 1

		return MatrixSparse(
			rows=self.cols,
			cols=self.rows,
			size=self.size,
			sparse=sparse
		)
	
	def transpose_fast(self):
		if self.sparse is None:
			return
		row_size = []
		row_start = [0]
		idx = 0
		while True:
			_sum = 0
			for t in self.sparse:
				if t.col == idx:
					_sum += 1
			row_size.append(_sum)
			if idx > 0:
				row_start.append(row_size[idx - 1] + row_start[idx - 1])
			if row_start[idx] + row_size[idx] == self.size:
				break
			idx += 1
		print(row_start)
		sparse = [Term() for _ in range(self.size)]
		for s in self.sparse:
			sparse[row_start[s.col]] = Term(s.col, s.row, s.value)
			row_start[s.col] += 1
		return MatrixSparse(
			rows=self.cols,
			cols=self.rows,
			size=self.size,
			sparse=sparse
		)

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
print("==================transpose=====================")
mat = mat.transpose()
print(mat)
print("==================transpose fast===================")
mat = mat.transpose_fast()
print(mat)