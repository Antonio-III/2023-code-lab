#Write a program that tests the user's exam marks between 0-100.
#If the mark is greater than 40, the output is "it's a pass", else, "it's a fail"
#Don't accept number > 100
#Extension: output "it's a merit" if marks is > 80.


marks = int(input("Enter your marks: ")) #Stores the input in variable "marks" and turns it into an integer 
                                         #(if the input string was a number)

while True:
    if marks > 100: #Checks first if the mark is greater than 100
        print("Number cannot be higher than 100")

    else:
       if marks > 80: #Marks > 80 is above because it has to be the first one to be checked
          print("It's a merit")

       elif marks > 40:
          print("It's a pass")
         
       else:
          print("It's a fail") 