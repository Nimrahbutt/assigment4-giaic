def double_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2

def main():
    numbers = [1, 2, 3, 4]
    double_numbers(numbers)
    print(numbers)

if __name__ == '__main__':
    main()
