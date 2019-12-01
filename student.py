students={"1ms17is100":"abc","1ms17is101":"aaa","1ms17is102":"abb"}
lst=["value1","value2","value3"]
lst2=[]
j=0
for i in students:
	print("key is ",i," Value is ",students[i])
	lst[j]=students[i]
	j=j+1

print(lst)
print(students.keys())
print(students.values())
print(students.items())

lst3={"1":3}
for n in lst3:
	print(n)
