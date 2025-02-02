print()
#speed Input
speed=int(input("ENTER YOUR SPEED (in Km/Hr): "))

print()

#Birthday ???
print("Do you have Happy Birthday Today ? ")
print("1.Yes")
print("2.No")

print()

#choice
choice=input("Enter Your Choice (1/2): ")

if choice == '2':
    if speed <=60:
        print(0," = No ticket")
        print("Thank You!")
    elif speed >=61 and speed <=80:
        print(1, "= Small ticket")
        print("Thank You!, Hope Not To See You Overspeeding Again")
    elif speed >=81:
        print(2, "= Big ticket")
        print("Thank You!, Hope Not To See You Overspeeding Again")
elif choice == '1':
    print("No charges Today, Happy Birthday !!!")
else:
    print("Invalid Choice")


print()
