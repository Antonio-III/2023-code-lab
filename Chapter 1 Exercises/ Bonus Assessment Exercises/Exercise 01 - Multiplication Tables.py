# Write a program to print Multiplication table in following format from 1 to 10 tables
# Hint: Use nested loops
# Multiplication table of : 1
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10

# Create a loop that ranges from numbers 1~10. This will determine the amount of rows we have, and the first factor for our multiplication
for x in range(1,11):
  print(f"This is the table of {x}!")
  
  # We create a nested loop ranging from numbers 1~10. This determines the numbers we will print. We will only use 1 column as well, so we will not be changing the 'end' argument of 'print()'
  for y in range(1,11):
    print(f"{x} x {y} = {x*y}!")

  # We put a 'print()' statement to create an empty space after the 'y' iteration finishes
  print()
  
