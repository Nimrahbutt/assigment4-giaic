def add_three_copies(my_list, data):
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():
    message = input("Enter a message to copy: ")
    
    # Initial list before adding
    my_list = []
    print(f"List before: {my_list}")
    
    # Call the function to add three copies of the data
    add_three_copies(my_list, message)
    
    # List after adding
    print(f"List after: {my_list}")

if __name__ == "__main__":
    main()
