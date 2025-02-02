i = False #not started
j = False #not stopped
while True:
    print("WELCOME TO THE CAR GAME")
    print(" Start \n Stop \n Quit \n Help")
    x = input("Select one:")
    if x == "Start":
        if i == True:
            print("Car has already started")
        else:
            print("Car is started.")
            i = True
            j = False
    elif x == "Stop":
        if j == True:
            print("Car has already stopped")
        else:
            print("Car has stopped.")
            j = True
            i = False
    elif x == "Help":
        print(" Select Start to start the car. \n Select Stop to stop the car. \n Select Quit to exit the game.")
    elif x == "Quit":
        break
print("Thankyou for playing.")