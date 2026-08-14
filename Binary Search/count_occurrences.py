# Count Occurrences

def lower_bound(arr, target):
    left = 0
    right = len(arr) - 1
    ans = len(arr)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


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


def count_occurrences(arr, target):
    lb = lower_bound(arr, target)

    if lb == len(arr) or arr[lb] != target:
        return 0

    ub = upper_bound(arr, target)

    return ub - lb


arr = [1, 2, 4, 4, 4, 7, 9]
target = 4

print(count_occurrences(arr, target))


# Time Complexity: O(log n)
# Space Complexity: O(1)