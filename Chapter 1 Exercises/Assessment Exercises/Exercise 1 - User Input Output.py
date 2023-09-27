#Write code to prompt the user to input her/his name and age and print these details on the screen. Find the length of the name and also the age of the user after one year.
#The format of text should look like the sample output below.
#(Use title() function) This is a method
#Hello, user!
#What is your name?
#alpha s
#What is your age?
#22
#It is good to meet you, Alpha S
#The length of your name is:
#5
#You will be 23 in a year.

name = input("Hello, user!\nWhat is your name? \n") #no whitespace between \n and "What" because it creates a blank space in the output
age = input("What is your age? \n") #you can use \n like this here because there is no letter after the \n that messes up the formatting
name_len = len(name) #to store the length of the name
age_one_year = age + 1 #used a variable to store so that all print functions use f-string formatting

print(f"It is good to meet you, {name.title()}!") #used .title() method to capitalize the first letters of the name
print(f"The length of your name is: \n{name_len}")
print(f"You will be {age_one_year} in a year.")
