from infix import Infix

if __name__ == "__main__":
	expr = "A-(B/((C*D)^E))"
	infix = Infix(expr)
	postfix = infix.translate_postfix()
	print(postfix)