def merge_sort(seq):
    if len(seq) < 2:
        return seq
    if len(seq) == 2:
        return [min(seq), max(seq)]
    m = len(seq)//2
    sorted1 = merge_sort(seq[:m])
    sorted2 = merge_sort(seq[m:])
    return sorted1 + sorted2


data = [10] * 100000000
sorted(data)
print("#1")
merge_sort(data)
print("#2")
