# Kth Missing Positive Number


# Direct Approach
def direct(arr, k):
    for i in range(len(arr)):
        if arr[i] <= k:
            k += 1
        else:
            break

    return k


# Formula-Based Approach
def kth_missing(arr, k):
    for i in range(len(arr)):
        missing = arr[i] - i - 1

        if missing >= k:
            return arr[i] - (missing - k) - 1

    return arr[-1] + (k - (arr[-1] - len(arr)))


# Optimal - Binary Search
def optimal_missing(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        missing = arr[mid] - (mid + 1)

        if missing < k:
            left = mid + 1
        else:
            right = mid - 1

    return left + k


arr = [2, 3, 4, 7, 11]
k = 5

print(direct(arr, k))
print(kth_missing(arr, k))
print(optimal_missing(arr, k))


# Direct Approach:
# Time Complexity: O(n)
# Space Complexity: O(1)

# Formula-Based Approach:
# Time Complexity: O(n)
# Space Complexity: O(1)

# Optimal:
# Time Complexity: O(log n)
# Space Complexity: O(1)