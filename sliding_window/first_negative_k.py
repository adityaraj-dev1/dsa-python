"""
Problem: First Negative Integer in Every Window of Size K

Approach 1: Brute Force
Time Complexity: O(n × k)
Space Complexity: O(1)

Approach 2: Sliding Window + Deque (Optimal)
Time Complexity: O(n)
Space Complexity: O(k)
"""

from collections import deque

# -------------------------------
# Approach 1: Brute Force
# -------------------------------
def first_negative_brute(arr, k):
    result = []

    for i in range(len(arr) - k + 1):
        found = False

        for j in range(i, i + k):
            if arr[j] < 0:
                result.append(arr[j])
                found = True
                break

        if not found:
            result.append(0)

    return result


# -------------------------------
# Approach 2: Sliding Window
# -------------------------------
def first_negative_optimal(arr, k):
    i = 0
    j = 0
    q = deque()
    result = []

    while j < len(arr):

        if arr[j] < 0:
            q.append(arr[j])

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:

            if not q:
                result.append(0)
            else:
                result.append(q[0])

            if q and q[0] == arr[i]:
                q.popleft()

            i += 1
            j += 1

    return result


# Driver Code
arr = [-1, 2, -3, -4, 5, 6, 7]
k = 3

print("Brute Force :", first_negative_brute(arr, k))
print("Optimal     :", first_negative_optimal(arr, k))