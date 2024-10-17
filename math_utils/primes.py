from math import isqrt

def isprime(n):
    """Tells us whether an integer is prime"""
    for i in range(1, isqrt(n)): #isqrt gives us the square root rounded down to the nearest integer
        if n % i == 0:
            return True
    return False