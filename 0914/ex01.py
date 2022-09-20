num = int(input())
sum_ = 0
for i in str(num):
	sum_ += int(i)
print(sum_)

# 자리수를 구하기 위한 코드
import math

BASE = 10

exp = int(math.log(num, BASE))
sum_ = 0
for i in range(exp, -1, -1):
	x = num // (10 ** i)
	sum_ += x
	num -= x * (10 ** i)

print(sum_)