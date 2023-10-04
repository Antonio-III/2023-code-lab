# Write a program to input three numbers and outputs the largest using the multiple if -else statements

three_nums = {"first":None,"second":None,"third":None} # Initialize a list that will collect the 3 numbers entered


for n in three_nums.keys(): # This for loop iterates as much as the amount of items in the list 
    entered_num = int(input(f"Input the {n} number: \n")) # Store the input number into the variable
    three_nums[n] = entered_num #add the entered nunmbers as the key's value
entered_nums = list(three_nums.values())
highest_num_index = entered_nums.index(max(entered_nums))
    
#Find the greatest number in the list using multiple if-else statements
if entered_nums[0] > entered_nums[1] and entered_nums[0] > entered_nums[2]: # Both conditions must be true for the first number to be the greatest
    print(f"The {number_place[index]} number is the greatest number, being {entered_nums[index]}.") # Outputs the greatest number as well as their position in the list
    
elif entered_nums[1] > entered_nums[0] and entered_nums[1] > entered_nums[2]:
    print(f"The {number_place[index]} number is the greatest number, being {entered_nums[index]}.")
    
elif entered_nums[2] > entered_nums[0] and entered_nums[2] > entered_nums[1]:
    print(f"The {number_place[index]} number is the greatest number, being {entered_nums[index]}.")

# In case of all numbers being equal or that there are 2 greatest numbers
else: 
    # All numbers are equal
    if entered_nums[0] == entered_nums[1] and entered_nums[0] == entered_nums[2]:
      print(f"All numbers are equal, those being {three_nums[index]}, {entered_nums[index+1]}, and {entered_nums[index+2]}.")
    # There are 2 greatest numbers

    elif entered_nums[0] == entered_nums[2]:
        print(f"The {number_place[index]} and {number_place[index+2]} numbers are both the greatest numbers, being {entered_nums[index]}.")
    else:
        print(f"The {number_place[index]} and {number_place[index+1]} numbers are both the greatest numbers, being {entered_nums[index]}.")
