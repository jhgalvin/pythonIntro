#create a function that checks which of two numbers is the maximum

def maximum(number1, number2):
    if(number1 > number2):
        return number1
    elif(number1 < number2):
        return number2
    else:
        print("The numbers are equal!")

print("Enter the first number: ")
number1 = int(input())

print("Enter the second number: ")
number2 = int(input())

max = maximum(number1, number2)
print("The greater number is {}!".format(max))