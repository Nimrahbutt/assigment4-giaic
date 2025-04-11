def add_many_numbers(numbers) -> int:
    total_so_far = 0
    for number in numbers:
        total_so_far += number
    return total_so_far

def main():
    numbers = [100, -50, 25, 75, -10, 30, -5]
    sum_of_numbers = add_many_numbers(numbers)
    print(sum_of_numbers)

if __name__ == '__main__':
    main()
