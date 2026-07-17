"""
Problem: Maximum Consecutive Ones

Given a binary array, return the maximum number
of consecutive 1's in the array.

Approach:
Single Traversal

Time Complexity: O(n)
Space Complexity: O(1)
"""


def maximum_consecutive_ones(arr):
    count = 0
    maximum = 0

    for num in arr:
        if num == 1:
            count += 1
            maximum = max(maximum, count)
        else:
            count = 0

    return maximum


# Driver Code
arr = [1, 1, 0, 1, 1, 1, 0, 1]
print("Maximum Consecutive Ones:", maximum_consecutive_ones(arr))