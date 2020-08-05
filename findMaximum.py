#create a function that checks which of two numbers is the maximum

def maximum(number1, number2):
    if(number1 > number2):
        print("The first number entered, {}, is greater!".format(number1))
    else:
        print("The second number entered, {}, is greater!".format(number2))

print("Enter the first number: ")
number1 = int(input())

print("Enter the second number: ")
number2 = int(input())

maximum(number1, number2)