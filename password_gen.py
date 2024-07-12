from random import choice
from string import printable

forbidden_symbols = set("aiuoeAIUOE")
allowed_symbols = set(printable).difference(forbidden_symbols)

sample = "".join(allowed_symbols)

try:
    length = int(input())
except ValueError:
    print("Error! Input must be a number!")
    exit()

n = 0
result = ""
while n < length:
    result = result + choice(sample)
    n = n + 1
print(result)
