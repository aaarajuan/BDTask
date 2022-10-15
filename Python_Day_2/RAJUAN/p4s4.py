x = [20, 30, 100, 150, 170, 525, 180, 50]
y = []

for i in x:
    if (i > 150): 
        continue # check if the numbers is greater than 150 than continue it.
    if (i > 500):
        break    # check if the numbers is greater than 500 than break it.
    if (i % 5 == 0): # check if the numbers from the 'x' list is divisible by 5
        y.append(i) # append the divisible numbers in the 'y' list by the following conditions
print(y) # print the 'y' list or divisible and satisfy numbers.
