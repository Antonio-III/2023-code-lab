#Enter your name and your age, and display an output
#Done using f-string formatting, way better than using commas (,) and concatenation (+)

first_name = input("Enter your first name: ") #Stores the value that represents your first name
last_name = input("Enter your last name: ") #Stores the value that represents your last name
full_name = (f"{first_name.title()} {last_name.title()}") #The value to represent your full name, but uppercased

print(f"Hello, {full_name}") #Outputs the value in the variable that stores your full name

age = int(input("Enter your age: ")) #Enter your age, only whole numbers allowed
print(f"Your name is {full_name}, and you are {age} years old") #Outputs your full name, along with your age
