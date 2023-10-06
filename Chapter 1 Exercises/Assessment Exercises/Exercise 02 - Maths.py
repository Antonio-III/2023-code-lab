#Write a program that evaluates the following calculations for two int numbers obtained from the user and outputs the results to the console:
#Sum (+) | Diff (-) | Product (x) | Quotient (/) | Remainder (%)

first_num = input(int("Enter a number \n"))
second_num = input(int("Enter a second number \n"))

sum = first_num + second_num
diff = first_num - second_num
prod = first_num * second_num
quo = first_num / second_num
rem = first_num % second_num

print(f"The first sum of the numbers is: {sum}!")
print(f"The first difference of the numbers is: {diff}!")
print(f"The first product of the numbers is: {prod}!")
print(f"The first quotient of the numbers is: {quo}!")
print(f"The first remainder of the numbers is: {rem}!")
