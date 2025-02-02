# Inputting the Number
n = int(input("Enter an interger Num: "))

# Deffining function
def addition(n):
    strConv = str(n)
    lstNo = list(map(int, strConv.strip()))
    return sum(lstNo)

# Calling the Function and Printing the Value
print(addition(n))