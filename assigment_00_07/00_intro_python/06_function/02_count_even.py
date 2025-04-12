def count_even():
    # Step 1: Ask for integers until the user presses enter
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            number = int(user_input)
            lst.append(number)
        except ValueError:
            print("Please enter a valid integer.")

    # Step 2: Count even numbers
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1

    # Step 3: Print the result
    print("Number of even numbers:", even_count)

# Run the function
if __name__ == "__main__":
    count_even()
