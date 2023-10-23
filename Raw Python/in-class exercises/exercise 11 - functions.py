#Copy this function
print("1.")
def greet_user(): #Define the function
    print("Hello!") #Write a statement/return value, when function is called

greet_user() #Call the function


print("\n") #For formatting the output to look cleaner

#Pass your name into a function
print("2.")
def greet_user(username): #Function with a parameter
    print(f"Hello, {username.title()}!") #Whatever is passed into the parameter, a ".title()" method is used

greet_user("antonio") #Calls the function while it passses the input into the parameter. Input being "antonio"


print("\n") #For formatting the output to look cleaner

#Input name from the user
print("3.")
def greet_user(username):
    print(f"Hello, {username.title()}!")

username = input("Enter your name: ")
greet_user(username)


print("\n") #For formatting the output to look cleaner


#Write a function called "favorite_film()" that accepts 1 parameter, "title". 
#It should print as: One of your facorite film is: - Avengers
print("4.")
def favorite_film(title):
    print(f"One of your favorite film is: - {title.title()}")

# title = input("Enter one of your favorite films:\n")

# favorite_film(title)

#OR to be more direct:
favorite_film(input("Enter one of your favorite films: "))


print("\n") #For formatting the output to look cleaner


#Create a sum of two numbers using sum() function (user-defined) with "return" type.
#Assign default values

print("5.")
def sum(a=10,b=5): #"a = 10" is assigning a default value
    return a+b #return type is used

print(f"The sum of the default values is {sum()}") #Only use the default values


print("\n") #For formatting the output to look cleaner

result = sum(20) #The number passed will be replacing the first argument's default value, being "10"
print(f"20 + 5 is {result}")


print("\n") #For formatting the output to look cleaner

result = sum(3,4) #Replace both of the default values
print(f"3 + 4 is {result}")


print("\n") #For formatting the output to look cleaner


#Returning a dictionary 
#Assign values to the following function and return the values in a dictionary format
def student(name,id,course="BSC CC"):
    student_name = {"name": name, "id": id, "course": course}
    return student_name

print(student("Antonio", 42))

#Pass this list variable to a function: usernames = ["Alpha", "Beta", "Gamma"] called greet_users()
# usernames = ["Alpha", "Beta", "Gamma"] #COMMENTED OUT
# def greet_users(names):                #COMMENTED OUT
#     return greet_users(names)          #COMMENTED OUT

# print(greet_users(usernames)) #PRINTS THE RETURN VALUE OF THE FUNCTION, THE RETURN VALUE CALLS THE FUNCTION, WHICH RETURNS THE FUNCITON AGAIN

#INSTEAD DO:
usernames = ["Alpha", "Beta", "Gamma"]
def greet_users(names): 
    print(f"{names[0]} likes the color red")
    print(f"{names[1]} likes the color blue")
    print(f"{names[2]} likes the color green")

greet_users(usernames)