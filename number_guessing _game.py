import random

secret_number = random.randint(1, 100)
guess = 0

# game logic
while True:
    try:
        # input
        player = int(input("Enter your guess from 1 to 100 here:"))
        guess +=1
        if player > secret_number:
            print("Too High!, Try Again.")
        elif player < secret_number:
            print("Too Low!, Try Again.")
        else:
            print(f"🎉 Congrats! You guessed the number in {guess} {'guess' if guess == 1 else 'guesses'}.")

    except ValueError:
        print("Invalid Input. Please enter a number from 1 to 100.")


