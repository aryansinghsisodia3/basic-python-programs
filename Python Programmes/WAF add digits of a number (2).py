# Inputting the Number
n = int(input("Enter an interger Num: "))

# Deffining function
def addition(n):
    sum=0
    for i in str(n):
        sum = sum + int(i)
    return sum

# Calling the Function and Printing the Value
print(addition(n))