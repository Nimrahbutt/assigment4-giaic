def main():
    # Dictionary of fruits and their prices
    fruit_prices = {
        "apple": 10.0,
        "durian": 35.0,
        "jackfruit": 20.5,
        "kiwi": 15.0,
        "rambutan": 7.5,
        "mango": 5.0
    }

    total_cost = 0.0

    # Loop through the dictionary and ask how many of each fruit the user wants
    for fruit, price in fruit_prices.items():
        try:
            quantity = int(input(f"How many ({fruit}) do you want?: "))
        except ValueError:
            print("Invalid input. Assuming 0.")
            quantity = 0
        total_cost += price * quantity

    print(f"\nYour total is ${total_cost}")

if __name__ == "__main__":
    main()
