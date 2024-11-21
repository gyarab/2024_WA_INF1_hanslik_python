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
    """
    Check if a number is prime.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    
    Raises:
    ValueError: If the input is not a positive integer.
    """
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    if number <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    if number <= 3:  # 2 and 3 are prime numbers
        return True
    if number % 2 == 0 or number % 3 == 0:  # Eliminate multiples of 2 and 3
        return False
    
    # Check divisors from 5 to √number
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
