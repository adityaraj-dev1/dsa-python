"""
Max Consecutive Ones III
LeetCode 1004

Given a binary array and an integer k, we can flip at most k zeros.
Find the maximum number of consecutive ones.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def longest_ones(arr, k):
    i = 0
    j = 0
    zeros = 0
    maximum = 0

    while j < len(arr):

        # Count zero entering the window
        if arr[j] == 0:
            zeros += 1

        # Shrink if more than k zeros
        while zeros > k:
            if arr[i] == 0:
                zeros -= 1
            i += 1

        # Current window is valid
        maximum = max(maximum, j - i + 1)

        j += 1

    return maximum


arr = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2

print(longest_ones(arr, k))