import math

BASE = 2
num_dec = 11
print(f"Decimal number = {num_dec}")

num_bin = ""
cnt_iter = int(math.log(num_dec, BASE))
while cnt_iter > 0:
	num_dec, r = num_dec // BASE, num_dec % BASE # 2로 나눈 몫과 나머지
	num_bin = str(r) + num_bin # 출력 문자열 구성
	cnt_iter -= 1
num_bin = str(num_dec) + num_bin
print(f"Binary number = {num_bin}")