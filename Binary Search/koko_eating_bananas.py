# Koko Eating Bananas

# Brute Force
def total_hours(piles, k):
    hours = 0

    for pile in piles:
        hours += (pile + k - 1) // k

    return hours


def koko_brute(piles, h):
    max_speed = max(piles)

    for k in range(1, max_speed + 1):
        if total_hours(piles, k) <= h:
            return k

    return -1


# Optimal - Binary Search
def koko(piles, h):
    left = 1
    right = max(piles)
    ans = right

    while left <= right:
        mid = (left + right) // 2

        if total_hours(piles, mid) <= h:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


piles = [3, 6, 7, 11]
h = 8

print(koko_brute(piles, h))  # 4
print(koko(piles, h))        # 4


# Brute Force:
# Time Complexity: O(n * max(piles))
# Space Complexity: O(1)

# Optimal:
# Time Complexity: O(n * log(max(piles)))
# Space Complexity: O(1)