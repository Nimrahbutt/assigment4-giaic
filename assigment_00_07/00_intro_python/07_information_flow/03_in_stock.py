def num_in_stock(fruit):
    # A dictionary representing Sophia's inventory
    inventory = {
        "apple": 50,
        "banana": 30,
        "pear": 1000,
        "mango": 200,
        "kiwi": 0
    }
    
    # Return the stock number for the fruit, or 0 if not found
    return inventory.get(fruit.lower(), 0)

def main():
    # Prompt the user for a fruit
    fruit = input("Enter a fruit: ").lower()
    
    # Get the number of fruits in stock
    stock_count = num_in_stock(fruit)
    
    # Print the result
    if stock_count > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock_count)
    else:
        print("This fruit is not in stock.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
