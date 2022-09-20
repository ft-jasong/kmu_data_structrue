BASE = 2 # 2진수
num_dec = 54 # 입력되는 10 진수
print(f"Decimal number = {num_dec}") # 입력 10진수 출력
num_bin = "" # 출력을 위한 공백 문자열을 준비

while num_dec > 1:
	num_dec, r = num_dec // BASE, num_dec % BASE # 2로 나눈 몫과 나머지
	num_bin = str(r) + num_bin # 출력 문자열 구성
num_bin = str(num_dec) + num_bin # 출력 문자열 구성

# # 총 3번의 나눗셈으로 구성
# # 1번째 나눗셈
# num_dec, r = num_dec // BASE, num_dec % BASE # 2로 나눈 몫과 나머지
# num_bin = str(r) + num_bin # 출력 문자열 구성
# # 2번째 나눗셈
# num_dec, r = num_dec // BASE, num_dec % BASE
# num_bin = str(r) + num_bin
# # 3번째 나눗셈
# num_dec, r = num_dec // BASE, num_dec % BASE
# num_bin = str(r) + num_bin
# # 마지막 나눗셈의 몫을 연결
# num_bin = str(num_dec) + num_bin #
# # 최종 계산된 2진수를 출력
print(f"Binary number = {num_bin}")