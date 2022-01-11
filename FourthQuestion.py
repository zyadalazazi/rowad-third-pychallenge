#Reading the input from the user
user_num = input("Please enter a number between 10 and 20:")

#Making sure that the input is a number
while not user_num.isnumeric():
    user_num = input("Do not enter characters, enter a number:")

#Checking the input and repeating the process if the input is invalid
valid = False
while not valid:
    if int(user_num) < 10:
        print("Too low")
        user_num = input("Enter a number between 10 and 20:")
    elif int(user_num) > 20:
        print("Too high")
        user_num = input("Enter a number between 10 and 20:")
    else:
        print("Thank you!")
        valid = True
