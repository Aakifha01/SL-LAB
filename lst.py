dictionary={
  "name":"Abc",
   "identity": "Student",
   "age": 17
}
print(dictionary)
key=dictionary["name"]
value=dictionary.get("name")
print("key is ",key)
print("value is ",value)
dictionary["name"]="aaa"
print(dictionary)
print(dictionary.keys())
