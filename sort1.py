a = [12, 2, -7, 22, 5]


def custom_sorting(seq):
    result = []
    while len(seq) > 0:
        min_n = seq[0]
        for n in seq:
            if n < min_n:
                min_n = n
        result.append(min_n)
        seq.remove(min_n)
    return result


print(custom_sorting(a))
