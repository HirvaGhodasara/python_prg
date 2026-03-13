def histogram(num_list):
    """
    Takes a list of integers and prints a histogram
    using asterisks to the screen.
    """
    for num in num_list:
        # Multiply the character '*' by the integer 'num'
        # to repeat it that many times.
        print('*' * num)

# Example usage based on your request:
histogram([4, 9, 7])
