# Create a loop that ranges from numbers 1~10. This will determine the amount of rows we have, and the first factor for our multiplication
for x in range(1,11):

  # We create a nested loop ranging from numbers 1~10. This determines the numbers we will print. We will only use 1 column as well, so we will not be changing the 'end' argument of 'print()'
  for y in range(1,11):
    print(f"{x} x {y}") 
