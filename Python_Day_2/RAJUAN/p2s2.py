x = int(input("Enter a number: "))
y = 0
for i in range(1, x + 1): # adding range user given number to 1 number greater so we can add user given number.
    y += i # using operator '+=' it's a short for of y = y + i.
print("Sum is: ", y) # printing the result