SIZE = 20
arr = [i for i in range(1, SIZE + 1)]
print(f"addr\t\tvalue")
for i in arr:
	print(f"{id(i):8}\t{i:2}")