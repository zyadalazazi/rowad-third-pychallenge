#Reading input from the user
user_num = input("Please input a number that is less than 50:")

#Making sure that the input is a number and less than 50
fl = False
while not fl:
    if not user_num.isnumeric():
        user_num = input("\nPlease input a number not a character:")
    elif int(user_num) > 50:
        user_num = input("\nThe number you entered is greater than 50, please enter a valid number:")
    else:
        fl = True

#Displaying the output
print("\nThe number you have entered is: {0}".format(user_num))
for x in range(int(user_num), 51):
    print(x, end=" ")