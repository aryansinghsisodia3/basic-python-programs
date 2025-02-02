#   INPUTS THE NUMBER ENTERED BY USER AS LIST
n=list(input("Enter The Number: "))

#   MAP FUNC() APPLIES int PROPERTY TO EVERY ELEMENT IN LIST (n)
l=list(map(int,n))

#   ADDITION i.e INITIAL VALUE = 0
a=0

#   MULTIPLICATION i.e INITIAL VALUE = 1
b=1

#   ENUMERATE FUNC() INDEX's THE LIST (l)
for i,j in enumerate(l):
    if i%2==0:
        a=a+j
    else:
        b=b*j

print() # TO GIVE SPACE

print("Sum of Odd Positioned Numbers", a)
print("Multiplication of Even Positioned Numbers", b)

print() # TO GIVE SPACE

print("Total Sum", a+b)