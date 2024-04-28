import random
def guessing_num():
    num = random.randint(1, 100)
    attempts = 0 
    print("Welcome to the Number Guessing Game!")
    print("Computer has chosen a number. Can you guess it?") 
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1 
        if guess < num:
            print("Too low.Try again.")
        elif guess > num:
            print("Too high.Try again.")
        else:
            print("Congratulations! You've guessed the number %d in %d attempts!"%(num,attempts))
            break
guessing_num()