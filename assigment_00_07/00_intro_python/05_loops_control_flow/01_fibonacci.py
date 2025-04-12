# Constant for the maximum value
MAX_VALUE = 10000

def print_fibonacci_up_to_max():
    a, b = 0, 1
    while a < MAX_VALUE:
        print(a, end=" ")
        a, b = b, a + b

if __name__ == "__main__":
    print_fibonacci_up_to_max()
