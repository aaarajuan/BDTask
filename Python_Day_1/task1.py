#task 1 Day 1:
# 1. first name
# 2. last name
# 3. college name
# 4. address
# there are different ways of printing those.

id12 = int(input('Enter the method no: ')) # used typecasting to convert input string to integer.

if (id12 == 1):
    # method no. 1
    print('ID NO. 12 Details:')
    print('First Name: Al-Arashad')
    print('Middle Name: Ahmed')
    print('Last Name: Rajuan')
    print('College Name: Comilla Polytechnic Institute (CPI)')
    print('Address: Karimunessa Road, Dogair, Sharulia-1361, Demra, Dhaka')

elif (id12 == 2):
    # method no. 2
    print('''ID NO. 12 Details:
    First Name: Al-Arashad
    Middle Name: Ahmed
    Last Name: Rajuan
    College Name: Comilla Polytechnic Institute(CPI)
    Address: Karimunessa Road, Dogair, Sharulia-1361, Demra, Dhaka''')
    # triple single qoutes for multiline printing in python.

elif (id12 == 3):
    # methond no. 3
    print('\nID NO. 12 Details: \nFirst Name: Al-Arashad\nMiddle Name: Ahmed\nLast Name: Rajuan\nCollege Name: Comilla Polytechnic Institute(CPI)\nAddress: Karimunessa Road, Dogair, Sharulia-1361, Demra, Dhaka')
    # \n opens a new line in python.

elif (id12 == 4):
    # method no. 4
    print('\nID NO. 12 Details: \n\tFirst Name: Al-Arashad\n\tMiddle Name: Ahmed\n\tLast Name: Rajuan\n\tCollege Name: Comilla Polytechnic Institute(CPI)\n\tAddress: Karimunessa Road, Dogair, Sharulia-1361, Demra, Dhaka')
    # using \n to open a new line and \t to tab in python.

else:
    print('Please Enter a Valid Method Number!!!')

