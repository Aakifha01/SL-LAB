class Student:
    def __init__(self):
        self.name=0
        self.age=0

    def display(self):
        print("Name is ",self.name)
        print("Age is",self.age)
        print("Marks is",self.marks)
    def accept(self):
        self.name=input("Enter name:")
        self.age=input("Enter age:")
        self.marks=input("Enter marks:")
        self.marks=list(self.marks.split(','))

p1=Student()
p1.accept()
p1.display()
        
