class Person:
	def __init__(self):
		self.name = ""
		self.age = 0
		self.salary = 0.0
	def __str__(self):
		return (f"{self.name}, {self.age}, {self.salary}")
	def setName(self, _name):
		self.name = _name;
	def setAge(self, _age):
		self.age = _age
	def setSalary(self, _salary):
		self.salary = _salary

james = Person()
james.setName("James")
james.setAge(20)
james.setSalary(100.0)
print(james)

edward = Person()
edward.setName("Edward")
edward.setAge(21)
edward.setSalary(200.0)
print(edward)