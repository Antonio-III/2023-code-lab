# Write Python Program to Find the Sum of Digits in a Number .For example if enters a number 1234 the result is 1+2+3+4 = 10

# For this exercise, we will make a function
def sum_of_digits(number):
 sum = 0
 while number > 0:
  
  sum += number % 10 # We will collect the number in the ones-place from the tens-place, hundreds, etc... And store it in a variable
  
  number = number//10 # We remove the current ones-place because it has already been added to the 'sum' variable. We use modulo division because normal division counts the decimal, modulo only counts the whole number, why is how 'number' will eventually reach 0. 
  
  return sum

num = int(input("Enter a number, and this program will find the sum of its digits! \n"))

print(f"The sum of the digits in {num} is... {sum_of_digits(num)}!")
  

