BASE = 2
num_dec = 11
print(f"Decimal number = {num_dec}")

num_bin = ""
while num_dec > 1:
	num_dec, r = num_dec // BASE, num_dec % BASE # 2로 나눈 몫과 나머지
	num_bin = str(r) + num_bin # 출력 문자열 구성
num_bin = str(num_dec) + num_bin
print(f"Binary number = {num_bin}")