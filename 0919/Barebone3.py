class Barebone:
	pass # pass는 안 좋은 습관.

bb_01 = Barebone()
print(id(bb_01))

bb_02 = Barebone()
print(id(bb_02))

bb_03 = bb_01
print(bb_01 is bb_02)
print(bb_01 is bb_03)