# Find Peak Element

# Brute Force
def peak_brute(arr):
    n = len(arr)

    for i in range(n):
        if (i == 0 or arr[i - 1] < arr[i]) and \
           (i == n - 1 or arr[i] > arr[i + 1]):
            return i

    return -1


# Optimal - Binary Search
def peak(arr):
    n = len(arr)

    if n == 1:
        return 0

    if arr[0] > arr[1]:
        return 0

    if arr[n - 1] > arr[n - 2]:
        return n - 1

    left = 1
    right = n - 2

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        elif arr[mid] > arr[mid - 1]:
            # We are climbing, so a peak exists on the right
            left = mid + 1

        else:
            # We are descending, so a peak exists on the left
            right = mid - 1

    return -1


arr = [1, 2, 3, 4, 5, 3, 1]

print(peak_brute(arr))
print(peak(arr))


# Brute Force:
# Time Complexity: O(n)
# Space Complexity: O(1)

# Optimal:
# Time Complexity: O(log n)
# Space Complexity: O(1)