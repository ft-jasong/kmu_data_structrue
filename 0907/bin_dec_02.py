num_bin = "1011"
print(f"Binary number = {num_bin}")

num_dec = 0
for c in num_bin:
	num_dec = num_dec * 2 + int(c)

print(f"Decimal number = {num_dec}")


# 교수님 방법

num_dec = 0
num_bin = num_bin[::-1] # 역방향으로 바꿔줌
cnt_iter = 0

while cnt_iter < len(num_bin):
	num_dec += 2 ** cnt_iter * int(num_bin[cnt_iter])
	cnt_iter += 1
print("----------------------------")
print(f"Decimal number = {num_dec}")
