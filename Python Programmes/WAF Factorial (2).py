# Inputing the number of which the factorial has to be found
num = int(input("Enter an interger Num: "))


# function for finding the factorial of any number
def Factorial(num):

    # Initialising factorial equals one
    factorial = 1
    
    if num < 0:   # First exception handled
        print("Factorial Doesn't exist for Negative Numbers.")
    elif num == 0:   # Second exception handled
        print("Factorial of Zero is One.")
    else:   # Factorial
        for i in range(1,num+1):
            factorial = factorial * i
        print("The Factorial of",num, "is", factorial)

# Calling the Function
Factorial(num)