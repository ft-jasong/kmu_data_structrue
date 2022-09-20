num_bin = "1011"
print(f"Binary number = {num_bin}")

num_dec = 0
for c in num_bin:
	num_dec *= 2
	num_dec += int(c)

print(f"Decimal number = {num_dec}")

# 교수님 box 설계방식
print("-------------교수님 방식-------------")
exp = 0
num_dec = 0
cnt_iter = len(num_bin)
while cnt_iter > 0:
	num_dec += 2**exp * int(num_bin[cnt_iter - 1])
	exp += 1
	cnt_iter -= 1
print(f"Decimal number = {num_dec}")
