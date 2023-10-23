#create a dictionary with your name and your id
student = {'Name':'Antonio','ID':'1337','Course':'CC'}


#use .items() function
for key, value in student.items():
    print("Key:", key)
    print("Value", value)

#use .keys() function
for key in student.keys(): #will print all keys
    print(key)

#use .values() function
for value in student.values(): #will print all values
    print(value)

#TO ADD ELEMENTS INTO DICTIONARIES.
student["Year of Entry"] = "2022"
print(student)

#CHANGE AN EXISTING VALUE
student['ID'] = "42"
print(student)

#DELETE A KEY-VALUE PAIR
del student['Course'] #just delete the key
print(student)