class Number:
    
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def display(self):
        print("Value:", self.value)

n1 = Number(10)
n2 = Number(5)

add_result = n1 + n2
sub_result = n1 - n2

print("Addition Result:")
add_result.display()

print("Subtraction Result:")
sub_result.display()
