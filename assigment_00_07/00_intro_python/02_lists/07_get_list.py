def main():
    values = []

    while True:
        user_input = input("Enter a value: ")
        if user_input == "":
            break
        values.append(user_input)

    print("Here's the list:", values)

if __name__ == "__main__":
    main()
