# data
# 0 1 1 0 0 0 0 0
# 1 0 0 1 0 0 0 0
# 1 0 0 1 0 0 0 0
# 0 1 1 0 0 0 0 0
# 0 0 0 0 0 1 0 0
# 0 0 0 0 1 0 1 0
# 0 0 0 0 0 1 0 1
# 0 0 0 0 0 0 1 0

class Node:
	def __init__(self, data):
		self.data = data
		self.link = None
	def __str__(self):
		return f"{self.data}"

class UndiGraph:
	def __init__(self, mat):
		self.mat = mat
		self.vertices = len(mat)
		self.linked = [None] * self.vertices
		self.__build()
	def __build(self):
		for row in range(self.vertices):
			for col in range(self.vertices):
				if self.mat[row][col] == 1:
					self.add_edge(row, col)
	def add_edge(self, src, dst):
		if self.linked[src] is None:
			self.linked[src] = Node(dst)
		else:
			search = self.linked[src]
			while search.link is not None:
				search = search.link
			search.link = Node(dst)
				
	def __str__(self):
		ret = ""
		for i, vt in enumerate(self.linked):
			ret += f"v[{i}] = "
			if vt is None:
				ret += "None\n"
				continue
			while vt is not None:
				ret += f"{vt}, "
				vt = vt.link
			ret += "\b\b \n"
		return ret

def read_input(name_file="input.dat"):
	mat = []
	with open(name_file) as f:
		for line in f:
			(*row,) = map(int, line.split())
			mat.append(row)
	return mat

def print_mat(mat):
	rows, cols = len(mat), len(mat[0])
	for row in range(rows):
		for col in range(cols):
			print(f"{mat[row][col]}", end=" ")
		print("\b")
if __name__ == "__main__":
	mat = read_input("input_g4.dat")
	print_mat(mat)
	print()
	print("Adjacency list")
	graph = UndiGraph(mat)
	print(graph)