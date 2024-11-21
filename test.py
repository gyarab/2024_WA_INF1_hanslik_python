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

def primes_in_range(start, end):
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

    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Both start and end must be integers.")
    if start > end:
        raise ValueError("Start must be less than or equal to end.")

    # Generate and return the list of primes
    try:
        return [num for num in range(start, end + 1) if is_prime(num)]
    except:
        raise ValueError()
