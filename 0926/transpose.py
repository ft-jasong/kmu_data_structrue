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