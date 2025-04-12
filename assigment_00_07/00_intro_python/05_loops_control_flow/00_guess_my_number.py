import random

def guess_my_number():
    number_to_guess = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            guess = int(input("Enter a guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < number_to_guess:
            print("Your guess is too low")
        elif guess > number_to_guess:
            print("Your guess is too high")
        else:
            print(f"Congrats! The number was: {number_to_guess}")
            break

if __name__ == "__main__":
    guess_my_number()
