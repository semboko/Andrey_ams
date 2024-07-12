numbers = []

while True:
    n = input()
    try:
        numbers.append(int(n))
    except ValueError:
        print("Invalid input")
        continue

    if int(n) < 0:
        print(sum(numbers))
        exit()
