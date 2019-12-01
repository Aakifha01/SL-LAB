class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

p1=Person("AAA",15)

print("\nName of the person 1 is ",p1.name)
print("\nAge of the person 1 is ",p1.age)

del p1.age

#print("P1 age:",p1.age)
print("p1 name:",p1.name)
#print(p1)

del p1
del Person
print("printing after deleting")
#print(p1)

p2=Person("aaa",15)
