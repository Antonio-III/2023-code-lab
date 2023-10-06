# Create an integer list and perform following operations
# - Create an int list with 10 values
# - Output the list using a for loop
# - Output the highest and lowest value
# - Sort the elements in ascending order
# - Sort the elements in descending order
# - Append two elements 
# - Print the list after appending

# Import these two functions (seed and randint) from the 'random' module. This is so that we can make a list with different variables for every run of the code
from random import seed
from random import randint

# We seed the later random number generator by giving it a random number from 0~10. If we do not give a seed to a random number generator, the seed of this 'randint()' will be the current system time in seconds or milliseconds. This will determine what integer our 'seed()' will get
seed(randint(0,10))

# Initialize a list with 10 values with random numbers. Random numbers are determined by the integer the 'seed()' (line 15) has, and the integer's seed is determined by the current system time
int_list = [randint(0,100) for i in range(10)]

# We output the list using a 'for loop'. It has 10 values so we will loop for 10 times
index_to_print = 0 # We create a variable to be incremented by 1 to be used in the 'for loop'
for loop in range(10):
  print(int_list[index_to_print])
  index_to_print+=1

# To output our highest value, we use the 'max()' function. To output our lowest value, we use the 'min()' function
highest_value = max(int_list)
lowest_value = min(int_list)
print(f"The highest number in our 'int' list is {highest_value} and the lowest is {lowest_value}!")


# To sort the elements in ascending order
sorted_list_asc = sorted(int_list)

# To sort the elements in descending order
sorted_list_desc = sorted(int_list, reverse = True)

# For appending two elements, I will use a the 'randint()' function
for x in range(2):
  int_list.append(randint(0,100))

# Then we print the list itself after appending
print(int_list)
