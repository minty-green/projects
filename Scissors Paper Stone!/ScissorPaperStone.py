import random

print("Scissors, Paper, Stone! \n"
      + "Scissors beats Paper \n"
      + "Paper beats Stone \n"
      + "Stone beats Scissors \n")

while True:
    print("Enter choice \n Scissors (1) \n Paper (2) \n Stone (3) \n")

    choice = int(input("User turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

    if choice == 1:
        choice_name = 'Scissors'
    elif choice == 2:
        choice_name = 'Paper'
    elif choice == 3:
        choice_name = 'Stone'

    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Scissors'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    elif comp_choice == 3:
        comp_choice_name = 'Stone'

    print("Computer choice is: " + comp_choice_name)

    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print(end="")
        result = "Scissors"

    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        print(end="")
        result = "Stone"
    else:
        print(end="")
        result = "Paper"

    if result == choice_name:
        print("User wins!")
    else:
        print("Computer wins!")

    print("Do you want to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break

print("\nThanks for playing")
