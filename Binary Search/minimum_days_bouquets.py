# Minimum Number of Days to Make M Bouquets


def possible(arr, day, m, k):
    count = 0
    bouquets = 0

    for flower in arr:
        if flower <= day:
            count += 1
        else:
            bouquets += count // k
            count = 0

    bouquets += count // k

    return bouquets >= m


# Brute Force
def bouquets_brute(arr, m, k):
    if len(arr) < m * k:
        return -1

    left = min(arr)
    right = max(arr)

    for day in range(left, right + 1):
        if possible(arr, day, m, k):
            return day

    return -1


# Optimal - Binary Search on Answer
def bouquets(arr, m, k):
    if len(arr) < m * k:
        return -1

    left = min(arr)
    right = max(arr)
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if possible(arr, mid, m, k):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


arr = [1, 3, 6, 2, 5, 8, 9, 7]
m = 2
k = 2

print(bouquets_brute(arr, m, k))
print(bouquets(arr, m, k))


# Brute Force:
# Time Complexity: O(n * (max(arr) - min(arr) + 1))
# Space Complexity: O(1)

# Optimal:
# Time Complexity: O(n * log(max(arr) - min(arr) + 1))
# Space Complexity: O(1)