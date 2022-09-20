class Barebone:
	pass # pass는 안 좋은 습관.

bb_01 = Barebone()
print(id(bb_01)) # address를 보려면 이라고 생각해도 된다.

bb_02 = Barebone()
print(id(bb_02))