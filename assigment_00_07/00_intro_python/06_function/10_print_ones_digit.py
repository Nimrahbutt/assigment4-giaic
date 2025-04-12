def print_ones_digit(num):
    # Use modulo to get the ones digit
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    # Prompt the user for an integer
    num = int(input("Enter a number: "))
    
    # Call the print_ones_digit function
    print_ones_digit(num)

# Run the main function
if __name__ == "__main__":
    main()
