BASE = 2

def binary(num, str):
	if num > BASE:
		binary(num // BASE, str)
		str = str + str(num % BASE)
	else:
		str = str + str(num)
	return str
bin = ""
bin = binary(11, bin)
print(bin)