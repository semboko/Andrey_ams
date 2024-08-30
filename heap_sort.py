def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def max_heapify(A, i, heap_size):
    l = left_child(i)
    r = right_child(i)
    largest = i
    if l < heap_size and A[l] > A[i]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)


def build_max_heap(A, heap_size):
    for i in range(len(A)//2 - 1, -1, -1):
        max_heapify(A, i, heap_size)


def heap_sort(A):
    heap_size = len(A)
    build_max_heap(A, heap_size)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        max_heapify(A, 0, heap_size)


numbers = [5, 17, 3, 27, 39, 82, 51, 3, 14, 99, 55]
heap_sort(numbers)
print(numbers)
