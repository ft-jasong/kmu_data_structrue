num = int(input())

sum_ = 0
while num != 0:
	sum_ += num % 10
	num = num // 10
print(sum_)