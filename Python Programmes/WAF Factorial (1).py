# Impoting factorial() function for math module
from math import factorial

# Inputing the number of which the factorial has to be found
num = int(input("Enter an interger Num: "))

# function for finding the factorial of any number
def Factorial(num):
    if num < 0:   # First exception handled
        print("Factorial Doesn't exist for Negative Numbers.")
    elif num == 0:   # Second exception handled
        print("Factorial of Zero is One.")
    elif num > 0:   # Factorial
        return factorial(num)

# printing and Calling the Function
print(Factorial(num))