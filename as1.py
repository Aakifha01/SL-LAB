#1
l1=['Hello',21,5.4,'Abc','Bye']
print("length of the list is",len(l1))

#2
l2=[l1,'Aakifha',22]
print("New list is",l2)

#3
print("printing second and third element using slice operator",l1[1:3])

#4
l1[1]='Apple'
print("List with fruit name",l1)

#5
print("Concating 2 lists",l1+l2)

#cloning using list method
l4=[2,3,4,5,6]
print("Original list is",l4)
print("Cloned list is",list(l4))

#cloning list using slice operator
l4=[2,3,4,5,6]
print("Original list is",l4)
print("Cloned list is",l4[:])

#split list into evenly sized chunks
mylist=list(range(1,11))

for i in range(0,len(mylist),2):
       print(mylist[i:i+2])


        

    

