def get_first_element(lst):
    print(lst[0])  # Prints the first element in the list

def main():
    lst = []
    num_elements = int(input("How many elements do you want to enter in the list? "))
    
    for _ in range(num_elements):
        element = input("Enter an element: ")
        lst.append(element)
    
    get_first_element(lst)  # Call the function to print the first element

if __name__ == "__main__":
    main()
