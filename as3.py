#Dictionary that holds details of students and printing details of students with even register numbers 
Student={
    21:{
        "name":'Aaki',
        "age":20,
        "section":'A'
    },
    36:{
        "name":'Amy',
        "age":20,
        "section":'A'
    },
    42:{
        "name":'HAnags',
        "age":20,
        "section":'A'
    },
    108:{
        "name":'Akhils',
        "age":20,
        "section":''
    }
}
print("Details of students with even register numbers")
for i in Student:
        if i%2==0:
           print(Student[i])
