def is_prime(number):
    x = 2
    while x < number:
        if number % x == 0:
            return False
        x = x + 1
    return True


n = 2
while (n < 1000):
    if is_prime(n):
        print(n)
    n = n + 1
