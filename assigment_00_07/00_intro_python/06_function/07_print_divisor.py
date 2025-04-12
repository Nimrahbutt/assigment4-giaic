def print_divisors(num):
    # Iterate through all numbers from 1 to num inclusive
    print(f"Here are the divisors of {num}:")
    for i in range(1, num + 1):
        if num % i == 0:  # Check if i is a divisor of num
            print(i, end=" ")  # Print the divisor with a space in between
    print()  # Newline after printing all divisors

def main():
    # Prompt the user for input
    num = int(input("Enter a number: "))
    
    # Call the print_divisors function
    print_divisors(num)

# Call the main function to run the program
if __name__ == "__main__":
    main()
