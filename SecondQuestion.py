#Reading input from the user
user_dir = input("Please enter the direction you want to go to (up or down):")

"""
Making sure that the inputs are from the correct datatype and are valid.
Also, Displaying the correct output.
"""
correct = False
while not correct:
    if user_dir == 'up':
        end_num = input("\nPlease enter a number:")
        while not end_num.isnumeric():
            end_num = input("Please enter a number not a character or a word:")
        for x in range(1, int(end_num) + 1):
            print(x, end=" ")
        correct = True

    elif user_dir == 'down':
        start_num = input("\nPlease enter a number below 20:")
        fl = False
        while not fl:
            if not start_num.isnumeric():
                start_num = input("\nPlease input a number not a character or a word:")
            elif int(start_num) >= 20:
                start_num = input("\nThe number you entered is 20 or greater, please enter a valid number:")
            else:
                for x in range(20, int(start_num), -1):
                    print(x, end=" ")
                fl = True
        correct = True

    else:
        print("\nI do not understand!")
        user_dir = input("Please enter the correct direction you want to go to (up or down):")
