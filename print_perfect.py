def is_perfect(number):
    x = 1
    s = 0
    while x <= number / 2:
        if number % x == 0:
            s = s + x
        x = x + 1
    if s == number:
        return True
    else:
        return False


print(is_perfect(6))  # Must be True
print(is_perfect(2))  # Must be False
print(is_perfect(28))  # Must be True
print(is_perfect(20))  # Must be False
