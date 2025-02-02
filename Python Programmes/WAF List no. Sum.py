# Initially there is an empty List
lst = []

# Inputting the number of elements
num = int(input('How many numbers: '))

# Inputting the List
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

# Calling the Function
print("The List thus formed is :", lst)
print("Sum of elements in given list is :", sum(lst))