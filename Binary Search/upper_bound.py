# Upper Bound
# Finds the first index where arr[index] > target

def upper_bound(arr, target):
    left = 0
    right = len(arr) - 1
    ans = len(arr)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


arr = [1, 2, 4, 4, 4, 7, 9]
target = 4

print(upper_bound(arr, target))


# Time Complexity: O(log n)
# Space Complexity: O(1)