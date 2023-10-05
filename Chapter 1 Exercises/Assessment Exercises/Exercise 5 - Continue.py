# Write a program that implements a while loop. This program should ask the user if they would like to continue and use the while loop to keep looping as long as they enter the letter Y. Once the while loop has terminated output the number of times it is executed.

# Initialize a counter
iterations = 0 

# Initialize a boolean to track if the user wants to exit the loop
exit_loop = False 

# Write the 'while loop' code block
while exit_loop == False:
  
  # Initialize a boolean to be used later in the code for another 'while loop'. It is placed inside the loop so its variable would reset per iteration
  invalid_char = True 
  
  if iterations == 1:
    enter_char = input(f"You are in a 'while loop'. You have looped {iterations} time. Would you like to loop another iteration? (y/n) \n")
  else:
    enter_char = input(f"You are in a 'while loop'. You have looped {iterations} times. Would you like to loop another iteration? (y/n) \n")

  # I created another 'while loop' and placed it inside the main loop because I want to have a different outcome when the user enters a different character than the ones given (y/n). So they will be looping this code without going to the next iteration if they keep entering an invalid character
  
  while invalid_char != False: #This is set up to always pass the condition of the boolean so we have to go through this loop at least once, for every iteration 
    if enter_char == 'y':
      invalid_char = False # We replaced the boolean value here because we need to fail the condition of this second loop, so we can continue to the next iteration of the main loop
      # Removed 'continue' statement in this line because even without it, once the last code has been executed (line 16), we will automatically go to another iteration
      
      iterations +=1 # We add integer 1 to the iterations since this marks the completion of 1 loop
    
    elif enter_char == 'n':
      exit_loop = True # Set boolean to fail the condition of the main loop
      break # Exit the loop we're currently in (the second 'while loop')
      
    else:
      # Initialize a variable that takes an input to see if the respone will be a valid character, else this code will keep executing. We don't need to change the boolean value to pass the condition of the second 'while loop' here because it already passes the condition. Adding it will not make a difference
      enter_char = input(f"Invalid input. Would you like to loop another iteration? (y/n) \n")
