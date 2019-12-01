lst=[1,2,3,4,5,6,7]
lst1=[77,33,44,55]
print("The length is ",len(lst))
lst.append(lst1)
print(lst)
print(lst[2:])
lst[1]="apple"
print(lst)

lst=lst+lst1
print(lst)

lst3=lst1
print("type 1 Copied list \n",lst3)

lst4=lst1.copy()
print("type 1 Copied list\n ",lst4)





tup=(1,2,3,4,5)
print(tup)
print(tup[1])



lst5=list(tup)
print(lst5)

