def main():
    MIN_HEIGHT = 50  # The minimum height required to ride

    while True:
        height = input("How tall are you? ")
        
        if height == "":
            break  # Stop asking if the user doesn't enter anything

        try:
            height = int(height)
            if height >= MIN_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
