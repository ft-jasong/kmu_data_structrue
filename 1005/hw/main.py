from infix import Infix

if __name__ == "__main__":
	expr = "A+B"
	infix = Infix(expr)
	postfix = infix.translate_postfix()
	print(postfix)