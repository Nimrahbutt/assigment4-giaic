def print_multiple(message, repeats):
    # Print the message 'repeats' number of times
    for _ in range(repeats):
        print(message)

def main():
    # Prompt the user for the message and the number of repeats
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Call the print_multiple function to print the message
    print_multiple(message, repeats)

# Call the main function to run the program
if __name__ == "__main__":
    main()
