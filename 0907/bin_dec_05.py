num_bin = "1011"
print(f"Binary number = {num_bin}")
num_bin = list(num_bin)

exp = 0
num_dec = 0
while num_bin:
	num_dec += 2**exp * int(num_bin.pop())
	exp += 1
print(f"Decimal number = {num_dec}")