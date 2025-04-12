# Define the constant ADULT_AGE
ADULT_AGE = 18

def is_adult(age):
    # Check if the age is greater than or equal to ADULT_AGE
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    # Ask the user for their age
    age = int(input("How old is this person?: "))
    
    # Call the is_adult function and print the result
    print(is_adult(age))

# Run the main function
if __name__ == "__main__":
    main()
