def double(num):
    return num * 2

def main():
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        result = double(number)
        print("Double that is", result)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
