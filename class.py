class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
p1=Person("AAA",15)
p2=Person("BBB",17)

print("\nName of the person 1 is ",p1.name)
print("\nAge of the person 1 is ",p1.age)

print("\nName of the person 2 is ",p2.name)
print("\nAge of the person 2 is ",p2.age)

p2.age=10
print("\nAge of the person 2 is ",p2.age)
