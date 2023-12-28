a = 5


def some_function():
    global a
    print(a)
    a = 6


some_function()
print(a)
