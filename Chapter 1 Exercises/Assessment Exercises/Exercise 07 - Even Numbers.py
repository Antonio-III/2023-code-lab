# Write a program that prints the even numbers from 1 to 100. 
# Hint - Use Continue Statement

#create a 'for loop' that iterates over a range containing numbers 1~100
for num in range(1,101):
  #if the current value of num, when divided by 2, returns 0, it will print the number
  if num % 2 == 0: 
    print(num)
  #if it fails the above condition, it will go back to the top of the loop (we use 'continue' statement here because python expects an indented code block)
  else:
    continue
