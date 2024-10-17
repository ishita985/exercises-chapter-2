from math import isqrt

def isprime(n):
    """Tells us whether an integer is prime"""
    if n == 1:
        return False
    else:
        for i in range(2, isqrt(n)): #isqrt gives us the square root rounded down to the nearest integer
            if n % i == 0:
                return False
        return True