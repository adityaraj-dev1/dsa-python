"""
Problem: Next Greater Element I
LeetCode: 496
Approach: Monotonic Stack + Dictionary

Time Complexity: O(n + m)
Space Complexity: O(n)

n = length of nums2
m = length of nums1
"""

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        stack = []
        nge = {}

        # Calculate NGE for nums2
        for x in nums2:

            while stack and stack[-1] < x:
                nge[stack.pop()] = x

            stack.append(x)

        # Elements remaining in stack have no NGE
        while stack:
            nge[stack.pop()] = -1

        # Answer queries from nums1
        result = []

        for x in nums1:
            result.append(nge[x])

        return result