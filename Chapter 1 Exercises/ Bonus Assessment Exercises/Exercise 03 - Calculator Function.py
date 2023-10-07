# The program should display the following calculator menu:

# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Modulus

 # The program will prompt the user to choose the operation choice (from 1 to 5). Then it asks the user to input values for the calculation. The program outputs the results of the calculation. The program should end by asking if the user would like to perform another calculation or not.

# We will define all our functions first
def add(x,y):
  return x + y

def subtract(x,y):
  return x - y

def multiply(x,y):
  return x * y

def divide(x,y):
  return x / y

def modulo(x,y):
  return x % y

# We will also make it a function to enter our two numbers
def operation():
  num_1 = int(input("Enter a number to represent our first number: \n"))
  num_2 = int(input("Enter a number to represent our second number: \n"))
  return num_1, num_2

# We will also make a string variable with placeholders for code reuse
result_txt = "The result of {} and {} performing {} is: {}!"

operations_txt = "Addition (1), Subtraction (2), Multiplication (3), Division (4), Modulus (5)"
start_txt = [f"For this exercise, we are going to create a 'calculator' program! Simply enter what number you'd like to operate: {operations_txt}", f"Enter what number you'd like to operate: {operations_txt}"]

# Initialize a counter to change texts when we loop for another time
iterations = 0

exit_main_loop = False

# We will put our code inside a 'while' loop
while exit_main_loop != True:
  exit_sec_loop = False
  
  if iterations == 0:
      enter_num = input(f"{start_txt[iterations]} \n")
  else:
    enter_num = input(f"{start_txt[iterations]} \n")

  if enter_num == '1':
      # Make a string variable to pass later on
      operation_str = "addition"
      
      # We assign the 2 returned values to these variables 
      first_num, sec_num = operation()

      result = add(first_num,sec_num) # Call the 'add()' function as we pass these 2 variables and store it in a variable

      # We pass 4 variables to replace our 4 placeholders using '.format()' method
      print(f"{result_txt.format(first_num,sec_num,operation_str,result)} \n")

  elif enter_num == '2':
      operation_str = "subtraction"
      
      first_num, sec_num = operation()

      result = subtract(first_num,sec_num)
      
      print(f"{result_txt.format(first_num,sec_num,operation_str,result)} \n")

  elif enter_num == '3':
      operation_str = "multiplication"
    
      first_num, sec_num = operation()

      result = multiply(first_num,sec_num) 

      print(f"{result_txt.format(first_num,sec_num,operation_str,result)} \n")

  elif enter_num == '4':
      operation_str = "divison"
      
      first_num, sec_num = operation()

      result = divide(first_num,sec_num) 

      print(f"{result_txt.format(first_num,sec_num,operation_str,result)} \n")

  elif enter_num == '5':
    operation_str = "modulo division"
     
    first_num, sec_num = operation()
    
    result = modulo(first_num,sec_num)
      
    print(f"{result_txt.format(first_num,sec_num,operation_str,result)} \n")

  while True:
    try_again = input("Would you like to perform another calculation? (y/n) \n")
    
    if try_again == 'y':
      iterations = 1 
      break # Leave the second loop, which will make up go back to the top of the main loop
      
    elif try_again == 'n':
      exit_main_loop = True # This will fail the condition when the program inevitably checks the 'while' loop condition 
      break # Exit this second loop
      
    else:
      continue # You will be stuck in this loop until you enter either 'y' or 'n'
  
 print() # We will create an empty space after every iteration

print("You've exited the loop!")
