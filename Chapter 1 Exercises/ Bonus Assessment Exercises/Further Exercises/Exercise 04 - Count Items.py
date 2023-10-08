# Write Python Program to Count the Number of Times an Item Appears in the List

# staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]

# (Hint: For each item in the list consider it as a key, and the number of times these items appear will be its associated value)

# We will initialize a boolean variable as we will need to control the flow of the loops later on. We will use 2 loops, a main one, and a nested
outer_loop = True
inner_loop = True

# Initialize a string list of names be checked which input is valid
staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]

# We make a function here because 'why not?'
def response_take(yn):
  global outer_loop # The names after the keyword 'global' are referring to the global variables. Meaning the variable is defined outside the function
  global inner_loop
  function_loop = True # This is a local variable. Meaning it is only defined inside the function. The only reason why we have this is for the 'else' section of the function

  while function_loop == True:
    if yn == 'y':
      inner_loop = False # This means for the next iteration, the inner loop's condition would be false
      function_loop = False # This means that we will not run the next iteration of this function, causing us to exit the function since there is none left to execute (notice how this 'while loop' is the last main code-block in the function)

    elif yn == 'n':
      # We fail all the conditions of all the loops so that we exit all the loop code-blocks in the next iteration (there won't be any)
      inner_loop = False
      outer_loop = False
      function_loop = False

    else:
      yn=input("Invalid response! Would you like to try again? (y/n) \n") # I used a local variable here because we want the function to keep updating the value of its local variable so that the user can eventually exit this function's loop (If they give a valid character). I got stuck in this section because I used the global var 'response'

    

print(f"For this exercise, we will count the amount of times a specific name appears in the list!")

while outer_loop == True:
  
  # Initialize this boolean var (inner_loop) inside the main 'while loop' so that its value resets per iteration
  inner_loop = True
  
  name = input("Enter whose name you'd like to count: 'Arshiya', 'Usman', 'Iftikhar', 'Rafia', 'Mary , 'Anmol', 'Zainab', 'Jake' \n")

  # We turn the input name into uppercase so that if it's a lowercase input, it is still valid
  input_name = name.title()

  # Check if the uppercased input matches any items in the list
  if input_name in staff:
    
    # Store the count inside a variable for efficiency (we don't have to type 'staff.count(input_name)' repeatedly)
    name_count = staff.count(input_name)
    
    print(f"The amount of times the name '{input_name}' appears on the list is... {name_count}!!! \n")
    response = input("That's all for this program! Would you like to try again? (y/n) \n")

    # We call on the function, passing an input var as the argument 
    response_take(response)

  else:
    while inner_loop == True:
      response=input("That name is not on the list, would you like to try again? (y/n) \n")
      response_take(response)

print("Thanks for playing!")
