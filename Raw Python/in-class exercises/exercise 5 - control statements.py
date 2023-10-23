age = int(input("Enter your age: ")) #Asks the user to enter age to be stored in the "age" variable
if age < 4 or age > 65: #Added OR statement to include "age > 65" in the control statement
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is %25.")
else:
    print("Your admission cost is $40.")