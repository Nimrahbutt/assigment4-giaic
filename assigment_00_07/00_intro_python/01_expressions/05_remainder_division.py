def main():
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    quotient = dividend // divisor
    remainder = dividend % divisor

    print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    main()
