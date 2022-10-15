# Write a program to print multiplication table of a given number.
n = int(input('Enter your number to see the multiplication: ')) # getting user input and type casting them from string to integer.

for x in range(1, 11): # using for loop and range function and adding range the number can be greater than or equals to 1 and smaller than 11.
    mt = n * x # multiplication and assgind that in a variable called 'mt'
    print(n, 'x', x, '=', mt) # printing the final result.