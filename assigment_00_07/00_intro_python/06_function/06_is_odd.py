def check_even_odd():
    for num in range(10, 20):
        if num % 2 == 0:
            print(f"{num} even", end=" ")
        else:
            print(f"{num} odd", end=" ")

def main():
    # Call the function to print even or odd for numbers from 10 to 19
    check_even_odd()

# Call the main function to execute the program
if __name__ == "__main__":
    main()
