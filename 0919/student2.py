class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self): # 문자열을 return하게 함. cpp에서 클래스 operator<< overloading 같음.
		return f"name is: {self.name}, {self.age}"

st = Student("Gildong Hong", 20)
print(st)