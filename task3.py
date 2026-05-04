import random
import timeit


# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def run_test(size):
    data = [random.randint(0, 10000) for _ in range(size)]

    print(f"\nРозмір масиву: {size}")

    print("Insertion Sort:",
          timeit.timeit(lambda: insertion_sort(data.copy()), number=1))

    print("Merge Sort:",
          timeit.timeit(lambda: merge_sort(data.copy()), number=1))

    print("Timsort (sorted):",
          timeit.timeit(lambda: sorted(data.copy()), number=1))


def main():
    for size in [100, 1000, 5000]:
        run_test(size)


if __name__ == "__main__":
    main()