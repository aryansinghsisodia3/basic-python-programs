# Program to check if a number is Palindrome


# Taking a int number from the user converting it into string
# And making it a list
numberEntered = list(str(input("Enter a Number: ")))

# Then reversing the list
reversedNumber = numberEntered[::-1]

# Now Checking if the reversed list is equal to the original list
if numberEntered==reversedNumber:
    print("Given Number is Palindrome")  # If the the reversed list is equal to 
                                         # the original list then the given number is Plaindrome

else:  # if the reversed list is not equal to the original list then not a Plaindrome
    print("Given Number is Not a Palindrome")