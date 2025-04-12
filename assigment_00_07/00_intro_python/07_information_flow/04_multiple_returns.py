def get_user_data():
    # Ask for the user's first name
    first_name = input("What is your first name?: ")
    
    # Ask for the user's last name
    last_name = input("What is your last name?: ")
    
    # Ask for the user's email address
    email = input("What is your email address?: ")
    
    # Return the user's data as a tuple
    return first_name, last_name, email

def main():
    # Call get_user_data to get the user's information
    user_data = get_user_data()
    
    # Print the received user data
    print("Received the following user data:", user_data)

# Run the main function to execute the program
if __name__ == "__main__":
    main()
