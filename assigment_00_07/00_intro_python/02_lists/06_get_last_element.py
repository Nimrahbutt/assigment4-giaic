def get_last_element(lst):
    print(lst[-1])  # Prints the last element in the list

def main():
    lst = []
    num_elements = int(input("How many elements do you want to enter in the list? "))
    
    for _ in range(num_elements):
        element = input("Enter an element: ")
        lst.append(element)
    
    get_last_element(lst)  # Call the function to print the last element

if __name__ == "__main__":
    main()
