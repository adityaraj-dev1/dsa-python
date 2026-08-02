"""
Fruit Into Baskets
LeetCode 904

Find the longest contiguous subarray containing at most
two distinct types of fruits.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def fruit_into_baskets(fruits):
    i = 0
    j = 0
    maximum = 0
    freq = {}

    while j < len(fruits):

        # Add current fruit to the window
        freq[fruits[j]] = freq.get(fruits[j], 0) + 1

        # More than 2 fruit types -> shrink window
        while len(freq) > 2:
            freq[fruits[i]] -= 1

            if freq[fruits[i]] == 0:
                del freq[fruits[i]]

            i += 1

        # Current window has at most 2 fruit types
        maximum = max(maximum, j - i + 1)

        j += 1

    return maximum


fruits = [1, 2, 1, 2, 3]

print(fruit_into_baskets(fruits))