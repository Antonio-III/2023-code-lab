# Write a program to input three numbers and outputs the largest using the multiple if -else statements

three_nums = [] # Initialize a list that will collect the 3 numbers entered
number_place = ["first", "second", "third"] # Initialize a list to count how many iterations (3) to perform. Gave names to represent the iteration count and their position in the list

for n in number_place: # This for loop iterates as much as the amount of items in the list 
    entered_num = int(input(f"Input the {n} number: \n")) # Store the input number into the variable
    three_nums.append(entered_num) # Add the input number to the first list
    index = three_nums.index(max(three_nums)) # Store the index value of the highest number in the list. To be used later 

#Find the greatest number in the list using multiple if-else statements
if three_nums[0] > three_nums[1] and three_nums[0] > three_nums[2]: # Both conditions must be true for the first number to be the greatest
    print(f"The {number_place[index]} number is the greatest number, being {three_nums[index]}.") # Outputs the greatest number as well as their position in the list
    
elif three_nums[1] > three_nums[0] and three_nums[1] > three_nums[2]:
    print(f"The {number_place[index]} number is the greatest number, being {three_nums[index]}.")
    
elif three_nums[2] > three_nums[0] and three_nums[2] > three_nums[1]:
    print(f"The {number_place[index]} number is the greatest number, being {three_nums[index]}.")

# In case of all numbers being equal or that there are 2 greatest numbers
else: 
    # All numbers are equal
    if three_nums[0] == three_nums[1] and three_nums[0] == three_nums[2]:
      print(f"All numbers are equal, those being {three_nums[index]}, {three_nums[index+1]}, and {three_nums[index+2]}.")
    # There are 2 greatest numbers
    else:
      print(f"The {number_place[index]} and {number_place[index+1]} numbers are the greatest number, being {three_nums[index]}.")
