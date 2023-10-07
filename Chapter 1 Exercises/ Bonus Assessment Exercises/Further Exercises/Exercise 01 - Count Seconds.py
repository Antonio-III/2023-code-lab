# Write a program that calculates the number of seconds in a day. Input a day, and calculate how many seconds there are? 
# Hint: Ask user to enter number of days, Convert days into hours, hours to minutes, minutes to seconds

print("In this exercise, we will turn the amount of days you give into seconds! \n")

# Initialize boolean to be used later
exit_loop = False

while exit_loop == False:
    
    # Initialize an input variable
    days = int(input("Enter the amount of days: \n"))
    
    days_to_seconds = days * 24 * 60 * 60
    
    print(f"The amount of seconds in the amount of days you entered is...{days_to_seconds}! \n")
    
    while True:
        
        try_again = input("Would you like to continue? (y/n) \n")
        
        if try_again == 'y':
            break

        elif try_again == 'n':
            exit_loop = True
            break

        else:
            print("Invalid character")
