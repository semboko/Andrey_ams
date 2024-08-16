class Coordinate:
    x: int
    y: int

    def __add__(self, other):
        result = Coordinate()
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result

    def __sub__(self, other):
        result = Coordinate()
        result.x = self.x - other.x
        result.y = self.y - other.y
        return result

    def __str__(self):
        return "Point: " + str(self.x) + "," + str(self.y)


x = list()
x.append(3)
x.append(5)
x.append(24)


a = Coordinate()
a.x = 240
a.y = -110


class Color:
    r: int = 0
    g: int = 0
    b: int = 0

    def represent(self):
        print(self.r, self.g, self.b)


b = Color()
b.r = 140
b.g = 255
b.b = 0

b1 = Color()


a = Coordinate()
a.x = 15
a.y = 14
b = Coordinate()
b.x = 0
b.y = 100

print(a)
print(b)

print(a + b)
print(a - b)
