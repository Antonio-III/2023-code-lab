#Write a program that asks the user to enter the lengths of the three sides of a triangle.
#Use the triangle inequality to determine if we have a triangle: In mathematics, the triangle inequality states that for any triangle, the sum of the lengths of any two sides must be greater than or equal to the length of #the remaining side (https://en.wikipedia.org/wiki/Triangle_inequality)
#Extension Problem (Optional):
#If valid, have the program correctly classify the type of triangle as either: Equilateral, Isosceles or Scalene (https://www.mathsisfun.com/triangle.html)

#Start of program
entered_triangle_sides = 0 #A counter to see how many sides have been input
triangle_sides = [] #Created a list to store all the sides that have been input 

while entered_triangle_sides <3: #Runs a loop to run the code below repeatedly
    triangle_side = int(input("Enter a triangle side:\n"))
    triangle_sides.append(triangle_side) #Adds the input number to the list
    entered_triangle_sides = entered_triangle_sides +1 #Once the code above has been executed, this will add a +1 to the variable on line 6
    

#Checks if the input sides pass the triangle inequality theorem
if triangle_sides[0] + triangle_sides[1] > triangle_sides[2] and triangle_sides[1] + triangle_sides[2] > triangle_sides[0] and triangle_sides[2] + triangle_sides[0] > triangle_sides[1]:
    
    print("You have entered a triangle! Congratulations!") #The input sides must pass the triangle inequality theorem for this to execute
    
    #This is for the extension problem. This executes if the condition (line 16) is met 
    if triangle_sides[0] == triangle_sides[1] and triangle_sides[1] == triangle_sides[2]:
        print("And you entered an Equilateral Triangle!")
    
    elif triangle_sides[0] == triangle_sides[1] or triangle_sides[1] == triangle_sides[2] or triangle_sides[2] == triangle_sides[0]:
        print("And you entered an Isosceles Triangle!")
        
    else:
        print("And you have entered a Scalene Triangle!")
    
else: 
    print("This is not a valid triangle! :((\nSad!")

    

    

    
