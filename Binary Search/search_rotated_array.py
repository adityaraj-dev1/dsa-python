# Search in Rotated Sorted Array

def search_rotated(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


arr = [6, 7, 1, 2, 3, 4, 5]
target = 7

print(search_rotated(arr, target))


# Time Complexity: O(log n)
# Space Complexity: O(1)