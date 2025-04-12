def in_range(n, low, high):
    """Returns True if n is between low and high, inclusive."""
    return low <= n <= high

def main():
    # Ask the user for a number and the range
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    # Check if the number is in the specified range
    if in_range(n, low, high):
        print(f"{n} is between {low} and {high}.")
    else:
        print(f"{n} is not between {low} and {high}.")

# Call the main function
if __name__ == "__main__":
    main()
