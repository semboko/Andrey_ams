def safe_pawns(coordinates):
    counter = 0
    for c in coordinates:
        x, y = c

        low_y = int(y) - 1

        x_left = chr(ord(x) - 1)
        x_right = chr(ord(x) + 1)

        def_left = x_left + str(low_y)
        def_right = x_right + str(low_y)

        if def_left in coordinates or def_right in coordinates:
            counter = counter + 1

    return counter


assert safe_pawns({"f4", "d4", "e3", "b4", "g5", "d2", "c3"}) == 6
assert safe_pawns({"f4", "c4", "b4", "e4", "g4", "d4", "e5"}) == 1
