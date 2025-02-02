# Inputting the Number
n = int(input("Enter an interger Num: "))

# Deffining function
def addition(n):
    sum=0
    while (n>0):
        sum=sum+n%10
        n = n//10
    return sum
# Calling the Function and Printing the Value
print(addition(n))