# Write a program to input three numbers and outputs the largest using the multiple if -else statements

three_nums = {"first":None,"second":None,"third":None} # Initialize a list that will collect the 3 numbers entered


for n in three_nums.keys(): # This for loop iterates as much as the amount of items in the list 
    entered_num = int(input(f"Input the {n} number: \n")) # Store the input number into the variable
    three_nums[n] = entered_num #add the entered nunmbers as the key's value
    
sorted_nums = dict(sorted(three_nums.items(), key = lambda item: item[1], reverse = True)) #Sort the dictionary by their values-pair in descending order by using a custom sorting key. This returns a list-type so we use dict() to convert the list into a dict-type

# Store the variable keys and values to these variables. 'desc' means 'descending'
desc_num_keys = list(sorted_nums.keys())
desc_num_values = list(sorted_nums.values())
    
# Find the greatest number in the list using multiple if-else statements.
if desc_num_values[0] > desc_num_values[1] and desc_num_values[0] > desc_num_values[2]: # Both conditions must be true for the code under to execute
    print(f"The {highest_num_keys} number is the highest, being {highest_num_values}") # Outputs the greatest number as well as their position in the list
    

# In case of all numbers being equal or that there are 2 greatest numbers
else: 
    # All numbers are equal
    if desc_num_values[0] == desc_num_values[1] and desc_num_values[0] == desc_num_values[2]:
      print(f"All numbers are equal, those being {desc_num_values[0]}, {desc_num_values[1]}, and {desc_num_values[2]}.")
        
    # There are 2 greatest numbers
    else:
        print(f"The {desc_num_keys[0]} and {desc_num_keys[1]} numbers are both the greatest numbers, being {desc_num_values[0]}.")
