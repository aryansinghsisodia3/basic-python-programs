n = int(input("Number of Students: "))
    
# FOUR GROPUS
grpA = 0
grpB = 0
grpC = 0
grpD = 0

for i in range(n):
    # INPUTTING THE AGE
    ageInput = int(input("Enter the Age: "))

    # Conditions
    if ageInput < 12:
        grpD = grpD + 1
    elif ageInput >= 12 and ageInput < 15:
        grpA = grpA + 1
    elif ageInput >= 15 and ageInput < 17:
        grpB = grpB + 1
    elif ageInput >= 17 and ageInput < 19:
        grpC = grpC + 1

# PRINTING STUFF

print("Students above 12 yrs and above but less than 15 yrs are: ", grpA)
print("Students above 15 yrs and above but less than 17 yrs are: ", grpB)
print("Students above 17 yrs and above but less than 19 yrs are: ", grpC)
print("Students lesser than 12 yrs are: ", grpD)