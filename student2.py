class Student:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def accept(self,marks):
		self.marks=marks
	def display(self):
		print("Name:",self.name)
		print("Age:",self.age)
		print("Marks:",self.marks)
	

print("Enter name")
name=input()
print("Enter age")
age=int(input())

st1=Student(name,age)
print("Enter the marks")
marks=list()
for i in range(6):
	print("Subject",i+1,":")
	marks.append(int(input()))
st1.accept(marks)
st1.display()


