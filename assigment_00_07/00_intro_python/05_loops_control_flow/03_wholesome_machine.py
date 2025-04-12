def main():
    affirmation = "I am capable of doing anything I put my mind to."
    print("Please type the following affirmation:")
    print(affirmation)
    
    while True:
        user_input = input()
        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm... That was not the affirmation. Please try again:")

if __name__ == "__main__":
    main()
