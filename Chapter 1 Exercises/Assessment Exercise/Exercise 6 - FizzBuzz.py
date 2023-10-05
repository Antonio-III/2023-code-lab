# Write a program that prints the numbers from 1 to 100. But for multiples of three print Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

# Create 'for loop' that iterates in a range function that contains the numbers from 1~100 
for num in range (1, 101):

  # We use modulo division to check if the 'num' variable would be a multiple of a number (3 in line 7). if the return is 0, it is indeed a multiple
  if num %% 3 == 0:
    print("Fizz")
  elif num %% 5 == 0:
    print("Buzz")
  elif num %% 5 == 0 and num %% 3 == 0:
    print("FizzBuzz")

  # If the iteration fails all the above conditions, it means it is not a multiple of 3 or 5, or both; so we print the number instead
  else:
    print(num)
