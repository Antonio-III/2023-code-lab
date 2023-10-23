# Code a program to display a menu on the screen that asks if the user wants to
# 1: Calculate the area of a square
# 2: Calculate the area of a circle
# 3: Calculate the area of a triangle 

# We will import the math module because we need a pi constant
from math import pi

# Initialize string variables. This will be the template of our sentences. For reuse purposes
start = "So, you've chosen to calculate the area of a {}! To calculate this, we need to {}."
input_param = "Enter a number to represent its"
result = "And the area of the {} with the parameters you entered is: {}!"

print(f"For this exercise, we will calculate the area of a square (1), circle (2), or triangle(3)! \n")

# Initialize an 'input' variable to determine which shape's area is to be calculated 
entered_num = (input("Enter a number to pick which shape's area you'd like to calculate: \n"))

print() # We want to create an empty space so our output looks cleaner
if entered_num == '1':
  
    # We initialize these variables because we will use the '.format()' method later on
    shape = "square"
    method = "multiply its width by its height"
    
    print(f"{start.format(shape,method)} \n") # You can see from the 'start' variable that it has empty curly brackets. These curly brackets will be filled with the values of the variables in line 23 and 24, hence the 2 arguments
    
    width = int(input(f"{input_param} width: \n"))
    height = int(input(f"{input_param} height: \n"))
    
    area = width * height

    print() # We want to create an empty space so our output looks cleaner
    
    print(f"{result.format(shape,area)} \n")

elif entered_num == '2':
    shape = "circle"
    method = "multiply its radius by pi"
    
    print(f"{start.format(shape,method)} \n")
    
    radius = int(input(f"{input_param} radius: \n"))
    
    area = radius * pi

    print() # We want to create an empty space so our output looks cleaner
    
    print(f"{result.format(shape,area)} \n")

elif entered_num == '3':
    shape = "triangle"
    method = "multiply its base by its height"
    
    print(f"{start.format(shape,method)} \n")
    
    base = int(input(f"{input_param} base: \n"))
    height = int(input(f"{input_param} height: \n"))
    
    area = base * height
    
    print() # We want to create an empty space so our output looks cleaner
    
    print(f"{result.format(shape,area)} \n")
