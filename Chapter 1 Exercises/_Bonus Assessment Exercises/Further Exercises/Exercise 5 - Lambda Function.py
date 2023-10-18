# Create the list marks with the given values

# marks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),("Smartphone Apps",68),("Games Development",70),("Responsive web",65)]
 
# Using lambda function in the function sort the list elements of the tuple based on marks low to high and high to low


# We intialize the 'marks' variable
marks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),("Smartphone Apps",68),("Games Development",70),("Responsive web",65)]
print(f"This is the 'marks' variable by default!: {marks} \n")

# We will use the 'sorted()' function with a custom key to sort by their tuple's second elements
marks_descending = sorted(marks,key = lambda item: item[1], reverse = True)
print(f"This is 'marks' arranged in descending by their second elements!: {marks_descending} \n")

# We will sort by ascending, but using the same custom key
marks_ascending = sorted(marks, key = lambda item: item[1])
print(f"This is 'marks' arranged in ascending order by their second elements!: {marks_ascending} \n")
