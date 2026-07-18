"""
Problem: Single Number (LeetCode 136)

Given a non-empty array of integers where every element appears twice
except for one, find that single element.
"""


# ----------------------------------------------------------
# Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# ----------------------------------------------------------

def single_num_brute(arr):
    for i in range(len(arr)):
        num = arr[i]
        count = 0

        for j in range(len(arr)):
            if arr[j] == num:
                count += 1

        if count == 1:
            return num


# ----------------------------------------------------------
# Hashing
# Time Complexity: O(n)
# Space Complexity: O(n)
# ----------------------------------------------------------

def single_num_hashing(arr):
    freq = {}

    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    for x in arr:
        if freq[x] == 1:
            return x


# ----------------------------------------------------------
# XOR (Optimal)
# Time Complexity: O(n)
# Space Complexity: O(1)
# ----------------------------------------------------------

def single_num_xor(arr):
    xor = 0

    for x in arr:
        xor ^= x

    return xor


# Driver Code
arr = [1, 1, 2, 2, 3, 4, 4]

print("Brute Force :", single_num_brute(arr))
print("Hashing     :", single_num_hashing(arr))
print("XOR         :", single_num_xor(arr))