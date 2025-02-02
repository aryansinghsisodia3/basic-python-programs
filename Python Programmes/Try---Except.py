a=float(input("Enter Your First Number: "))
b=float(input("Enter Your Second Number: "))

try:
    print(a, "Divided by", b,"is", a/b)
except:
    ZeroDivisionError
    print("You Cannot Divide By Zero")