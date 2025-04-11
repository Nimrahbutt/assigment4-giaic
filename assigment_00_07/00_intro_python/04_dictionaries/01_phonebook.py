def add_contact(phonebook):
    name = input("Enter the name of the contact: ")
    phone_number = input("Enter the phone number: ")
    phonebook[name] = phone_number
    print(f"Contact {name} added successfully.")

def search_contact(phonebook):
    name = input("Enter the name to search: ")
    if name in phonebook:
        print(f"{name}'s phone number is: {phonebook[name]}")
    else:
        print(f"Contact {name} not found.")

def display_phonebook(phonebook):
    if phonebook:
        print("Phonebook contents:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("The phonebook is empty.")

def main():
    phonebook = {}  # Create an empty phonebook dictionary
    
    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Phonebook")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            search_contact(phonebook)
        elif choice == "3":
            display_phonebook(phonebook)
        elif choice == "4":
            print("Exiting the phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
