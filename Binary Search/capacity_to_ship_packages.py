# Capacity to Ship Packages Within D Days


def days_required(arr, capacity):
    load = 0
    days = 1

    for weight in arr:
        if load + weight > capacity:
            days += 1
            load = weight
        else:
            load += weight

    return days


# Brute Force
def brute(arr, d):
    for capacity in range(max(arr), sum(arr) + 1):
        if days_required(arr, capacity) <= d:
            return capacity

    return -1


# Optimal - Binary Search
def optimal(arr, d):
    left = max(arr)
    right = sum(arr)
    ans = right

    while left <= right:
        mid = (left + right) // 2

        if days_required(arr, mid) <= d:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
d = 5

print(brute(arr, d))
print(optimal(arr, d))


# Brute Force:
# Time Complexity: O(n * (sum(arr) - max(arr) + 1))
# Space Complexity: O(1)

# Optimal:
# Time Complexity: O(n * log(sum(arr) - max(arr) + 1))
# Space Complexity: O(1)