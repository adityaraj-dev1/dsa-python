# First and Last Occurrence

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


def first_last(arr, target):
    lb = lower_bound(arr, target)

    # Target does not exist
    if lb == len(arr) or arr[lb] != target:
        return [-1, -1]

    ub = upper_bound(arr, target)

    return [lb, ub - 1]


arr = [1, 2, 4, 4, 4, 7, 9]
target = 4

print(first_last(arr, target))


# Time Complexity: O(log n)
# Space Complexity: O(1)