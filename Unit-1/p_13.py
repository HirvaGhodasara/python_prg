from functools import reduce

def main():
    # Initial list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original List: {numbers}")
    print("-" * 30)

    # 1. MAP(): Apply a function to every item
    # Task: Square every number in the list
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print(f"1. MAP (Squared):      {squared_numbers}")

    # 2. FILTER(): Select items based on a condition
    # Task: Keep only numbers that are greater than 5
    big_numbers = list(filter(lambda x: x > 5, numbers))
    print(f"2. FILTER (> 5):       {big_numbers}")

    # 3. REDUCE(): Combine all items into a single value
    # Task: Calculate the sum of all numbers
    # Note: reduce takes two arguments (accumulator, current_value)
    total_sum = reduce(lambda acc, val: acc + val, numbers)
    print(f"3. REDUCE (Total Sum): {total_sum}")

if __name__ == "__main__":
    main()
