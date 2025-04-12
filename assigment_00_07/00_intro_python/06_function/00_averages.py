def find_average(num1, num2):
    return (num1 + num2) / 2

def main():
    # Ask the user for two numbers
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    
    # Find the average
    average = find_average(number1, number2)
    
    # Print the result
    print("The average is:", average)

if __name__ == "__main__":
    main()
