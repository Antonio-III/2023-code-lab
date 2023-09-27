#Write a program that asks the user to enter the lengths of the three sides of a triangle.
#Use the triangle inequality to determine if we have a triangle: In mathematics, the triangle inequality states that for any triangle, the sum of the lengths of any two sides must be greater than or equal to the length of #the remaining side (https://en.wikipedia.org/wiki/Triangle_inequality)
#Extension Problem (Optional):
#If valid, have the program correctly classify the type of triangle as either: Equilateral, Isosceles or Scalene (https://www.mathsisfun.com/triangle.html)

entered_triangle_sides = 0
triangle_sides = []

while entered_triangle_sides <3:
    triangle_side = int(input("Enter a triangle side:\n"))
    entered_triangle_sides = entered_triangle_sides +1
    triangle_sides.append(triangle_side)

if triangle_sides[0] + triangle_sides[1] > triangle_sides[2]:
    triangle_check = True
    
elif triangle_sides[1] + triangle_sides[2] > triangle_sides[0]:
    triangle_check = True
    
elif triangle_sides[2] + triangle_sides[0] > triangle_sides[1]:
    triangle_check = True
    
else:
    triangle_check = False
    

if triangle_check == True:
    
    print("You have entered a triangle! Congratulations!")

  #this is for the extension problem
    if triangle_sides[0] == triangle_sides[1] and triangle_sides[1] == triangle_sides[2]:
        print("You entered an Equilateral Triangle!")
    
    elif triangle_sides[0] == triangle_sides[1] or triangle_sides[1] == triangle_sides[2] or triangle_sides[2] == triangle_sides[0]:
        print("You entered an Isosceles Triangle!")
        
    else:
        print("You have entered a Scalene Triangle!")
    
else: 
    print("This is not a valid triangle! :((\nSad!")

    

    

    
