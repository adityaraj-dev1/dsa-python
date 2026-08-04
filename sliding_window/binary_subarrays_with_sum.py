"""
LeetCode 930 - Binary Subarrays With Sum

Count contiguous subarrays whose sum is exactly equal to goal.

Exactly(goal) = AtMost(goal) - AtMost(goal - 1)

Time Complexity: O(n)
Space Complexity: O(1)
"""


def binary_subarrays(nums, goal):

    def at_most(k):
        if k < 0:
            return 0

        i = 0
        j = 0
        current_sum = 0
        count = 0

        while j < len(nums):
            current_sum += nums[j]

            while current_sum > k:
                current_sum -= nums[i]
                i += 1

            count += j - i + 1
            j += 1

        return count

    return at_most(goal) - at_most(goal - 1)


nums = [1, 0, 1, 0, 1]
goal = 2

print(binary_subarrays(nums, goal))