MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()
        print(f"Removed: {removed}")
    print(f"Final list: {lst}")

def main():
    num_elements = int(input("How many elements in your list? "))
    lst = []
    for _ in range(num_elements):
        item = input("Enter an element: ")
        lst.append(item)

    print(f"Original list: {lst}")
    shorten(lst)

if __name__ == "__main__":
    main()
