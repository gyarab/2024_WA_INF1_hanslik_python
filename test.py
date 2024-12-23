def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    except:
        raise(ValueError)

def celsius_to_fahrenheit(celsius):
    try:
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit
    except:
        raise(ValueError)


def is_prime(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be an integer")
    else:
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

def primes_in_range(a, b):
    if not isinstance(a, int) or not isinstance(b, int) or a < 0 or b < 0:
        raise ValueError("a and b must be non-negative integers")
    if a > b:
        a, b = b, a
    return [n for n in range(a, b+1) if is_prime(n)]
