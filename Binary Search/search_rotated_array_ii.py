# Search in Rotated Sorted Array II

def search_rotated(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True

        # Duplicates make it impossible to determine
        # which half is sorted
        if arr[left] == arr[mid] == arr[right]:
            left += 1
            right -= 1
            continue

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

    return False


arr = [2, 5, 6, 0, 0, 1, 2]
target = 0

print(search_rotated(arr, target))


# Time Complexity: O(log n) average
# Worst-case Time Complexity: O(n)
# Space Complexity: O(1)