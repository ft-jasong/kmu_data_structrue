num_bin = "1011"
print(f"Binary number = {num_bin}")

BIT = 3
num_bin = num_bin[::-1]
num_oct = []
remain = len(num_bin)
# while (remain >= BIT):
# 	for ()
# 	remain -=3

# 교수님 코드

cnt_bit = 0
while cnt_bit < len(num_bin):
	cnt, sum_ = 0, 0

	while cnt < BIT:
		if cnt_bit >= len(num_bin):
			break

		sum_ += 2 ** cnt * int(num_bin[cnt_bit])
		cnt += 1
		cnt_bit += 1

	num_oct.append(sum_)

num_oct = num_oct[::-1]
num_oct = "".join(map(str, num_oct))
print(f"Octal number = {num_oct}")