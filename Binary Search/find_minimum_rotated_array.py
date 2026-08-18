# Find Minimum in Rotated Sorted Array

def find_min(arr):
    left = 0
    right = len(arr) - 1

    while left < right:

        # Current search space is already sorted
        if arr[left] <= arr[right]:
            return arr[left]

        mid = (left + right) // 2

        # Left half is sorted
        if arr[left] <= arr[mid]:
            left = mid + 1

        # Minimum is in the left half
        else:
            right = mid

    return arr[left]


arr = [4, 5, 6, 7, 0, 1, 2]

print(find_min(arr))


# Time Complexity: O(log n)
# Space Complexity: O(1)