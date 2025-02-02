emptyList=[] # Empty list

# for loop to iterate between 1500 & 2700 (included)
for x in range(1500, 2701):
    
    # Checking if the digit is divisible by 7 and 5,
    # if (true) then appending the number to the empty list
    if (x%7 == 0) and (x%5 != 0):  
        emptyList.append(str(x))

# then simply add comma after each number
print (','.join(emptyList))