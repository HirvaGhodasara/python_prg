from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# map() → square of each number
square = list(map(lambda x: x*x, nums))
print("Squares:", square)

# filter() → only even numbers
even = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", even)

# reduce() → sum of all numbers
total = reduce(lambda a, b: a + b, nums)
print("Total sum:", total)
