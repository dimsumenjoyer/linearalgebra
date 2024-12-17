def func(x, y):
    return (x + y + x * y)

# Function for euler formula
def euler(x0, y, h, x):
    temp = -0
    # Iterating till the point at which we
    # need approximation
    while x0 < x:
        temp = y
        y = y + h * func(x0, y)
        x0 = x0 + h
    # Printing approximation
    print(f"Approximate solution at x = {x} is {y}.")
    return

# Driver Code
# Initial Values

x0 = 0
y0 = 1
h = 0.025

# Value of x at which we need approximation
x = 0.1
euler(x0, y0, h, x)