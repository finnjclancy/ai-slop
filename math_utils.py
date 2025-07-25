def square(x):
    """Return the square of a number"""
    return x * x

def cube(x):
    """Return the cube of a number"""
    return x * x * x

def factorial(n):
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1) 