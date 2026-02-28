number_toolkit_utils.py

print("Hello, World!")
# number_toolkit_utils.py

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def factors(n):
    return [i for i in range(1, n+1) if n % i == 0]

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a+b
    return sequence
