x = 70   # Global variable

def demo():
    y = 50   # Local variable
    print("Local y =", y)

    global x
    x = x + 5
    print("Global x =", x)

    def inner():
        nonlocal y
        y = y + 10
        print("Nonlocal y =", y)

    inner()

demo()
