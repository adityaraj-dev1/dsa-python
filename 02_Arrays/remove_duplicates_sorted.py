def remove_duplicates(arr):
    if len(arr) == 0:
        return 0

    i = 0
    n = len(arr)

    for j in range(1, n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1


arr = [1, 1, 2, 2, 3, 3, 4]
length = remove_duplicates(arr)

print("Array after removing duplicates:", arr[:length])
