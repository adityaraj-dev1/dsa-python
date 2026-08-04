"""
LeetCode 713 - Subarray Product Less Than K

Count contiguous subarrays whose product is strictly less than k.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def subarray_product(nums, k):
    if k <= 1:
        return 0

    i = 0
    j = 0
    current_product = 1
    count = 0

    while j < len(nums):
        current_product *= nums[j]

        while current_product >= k:
            current_product //= nums[i]
            i += 1

        count += j - i + 1
        j += 1

    return count


nums = [10, 5, 2, 6]
k = 100

print(subarray_product(nums, k))