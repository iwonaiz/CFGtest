print("Please select operation -\n "
"1. Add\n "
"2. Subtract\n"
"3. Multiply\n"
"4. Divide\n")
# Take input from the user
select = input("Select operations form 1, 2, 3, 4 :").strip()
number_1 = int(input("Enter first number: ").strip())
number_2 = int(input("Enter second number: ").strip())


# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers

def substract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
# Function to divide two numbers

def divide(num1, num2):
    return num1 / num2
# Calculator logic
if select == '1':
    print(add(number_1, number_2))
elif select == '2':
    print(substract(number_1, number_2))
elif select == '3':
    print(multiply(number_1, number_2))
elif select == '4':
    print(divide(number_1, number_2))
else:
    print('You have not entered a valid number')