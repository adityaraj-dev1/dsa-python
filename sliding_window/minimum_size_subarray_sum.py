"""
Minimum Size Subarray Sum
LeetCode 209

Find the minimum length of a contiguous subarray whose
sum is greater than or equal to target.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def minimum_subarray(arr, target):
    i = 0
    j = 0
    current_sum = 0
    minimum = float('inf')

    while j < len(arr):
        # Expand window
        current_sum += arr[j]

        # Shrink while the window satisfies the target
        while current_sum >= target:
            minimum = min(minimum, j - i + 1)

            current_sum -= arr[i]
            i += 1

        j += 1

    # No valid subarray found
    return 0 if minimum == float('inf') else minimum


arr = [2, 3, 1, 2, 4, 3]
target = 7

print(minimum_subarray(arr, target))