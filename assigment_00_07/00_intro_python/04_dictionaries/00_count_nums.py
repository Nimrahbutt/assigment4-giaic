def main():
    number_count = {}  # Dictionary to store the count of each number

    while True:
        user_input = input("Enter a number: ")
        if user_input == "":  # If the user presses enter without typing a number, break the loop
            break
        number = int(user_input)  # Convert the input to an integer
        if number in number_count:
            number_count[number] += 1  # If the number already exists in the dictionary, increment its count
        else:
            number_count[number] = 1  # If the number is not in the dictionary, add it with count 1

    # Print the counts of each number
    for number, count in number_count.items():
        print(f"{number} appears {count} times.")

if __name__ == "__main__":
    main()
