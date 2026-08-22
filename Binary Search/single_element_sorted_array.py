# Single Element in a Sorted Array

def single_element(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        # Make mid even
        if mid % 2 == 1:
            mid -= 1

        # Pair is correct
        if arr[mid] == arr[mid + 1]:
            left = mid + 2

        # Pair is broken
        else:
            right = mid

    return arr[left]


arr = [1, 1, 2, 2, 3, 4, 4, 5, 5]

print(single_element(arr))


# Time Complexity: O(log n)
# Space Complexity: O(1)