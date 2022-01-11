#Initializing the invitees list and reading input from the user
invitees = []
inv_num = input("Please enter the number of users you want to invite (less than 10):")

#Making sure that the input is valid (a number)
while not inv_num.isnumeric():
    print("Invalid!")
    inv_num = input("Please enter a number:")

#Checking the input and printing the appropriate output
if int(inv_num) < 1:
    print("You need to invite people, please rerun the program and enter a number greater than 0.")

elif int(inv_num) < 10:
    for i in range(0, int(inv_num)):
        invitees.append(input("Please input the name of the guest number {0}:".format(i+1)))
        print("{0} has been invited".format(invitees[-1]))
    print("All the people you added have been invited :)")

else:
    print("Too many people, please re-run the program and enter a number less than 10.")
