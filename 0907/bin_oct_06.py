def convert_bin_to_octal(num_bin):
	BIT = 3
	num_oct = []
	octal = []

	while num_bin:
		cnt, sum_ = 0, 0
		while cnt < BIT and num_bin:
			octal.append(int(num_bin.pop()))
			cnt += 1

		cnt = 0
		while octal:
			bin_ = octal.pop(0)
			sum_ += 2**cnt * bin_
			cnt += 1

		num_oct.append(sum_)

	num_oct = "".join(map(str, num_oct[::-1]))
	print(f"Octal number = {num_oct}")

str_bin = "1011"