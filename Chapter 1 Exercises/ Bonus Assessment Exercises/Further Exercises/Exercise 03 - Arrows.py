# Write a Python program to print the asterisk pattern shown below
#     *
#    ***
#   *****
#  *******
# *********
#    ***  
#    ***
#    ***

# Create a loop. This will be the amount of rows we have. We will not create a nested loop because we will not need it. Every iterations end in a new line and inside those iterations are our 'columns'
for x in range(8):
    if x < 5:
        spaces = " " * 3
        star = "*" * (x * 2 + 1)
        print(spaces+star)
        spaces -=1    
    else:
        spaces = " " * 3
        star  = "*" * 3
        print(spaces+star)
