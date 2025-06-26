import random

secret_number = random.randint(1, 100)

# game logic
while True:
    try:
        # input
        player = int(input("Enter your guess from 1 to 100 here:"))
        if player > secret_number:
            print("Too High!, Try Again.")
        elif player < secret_number:
            print("Too Low!, Try Again.")
        else:
            print("Please enter a number between 1 to 100.")
    except ValueError:
        print("Invalid Input. Please enter a number from 1 to 100.")


