"""
Problem: Missing Number

Given an array containing n-1 distinct numbers from 1 to n,
find the missing number.

Approaches:
1. Brute Force
2. Hashing
3. Sum Formula
4. XOR
"""


# -------------------------------
# Brute Force
# Time Complexity: O(n²)
# Space Complexity: O(1)
# -------------------------------
def brute(arr, n):
    for i in range(1, n + 1):
        found = False
        for num in arr:
            if num == i:
                found = True
                break
        if not found:
            return i


# -------------------------------
# Hashing
# Time Complexity: O(n)
# Space Complexity: O(n)
# -------------------------------
def hashing(arr, n):
    freq = [0] * (n + 1)

    for num in arr:
        freq[num] = 1

    for i in range(1, n + 1):
        if freq[i] == 0:
            return i


# -------------------------------
# Sum Formula
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------
def sum_formula(arr, n):
    total_sum = n * (n + 1) // 2
    array_sum = sum(arr)

    return total_sum - array_sum


# -------------------------------
# XOR
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------
def xor_method(arr, n):
    xor1 = 0
    xor2 = 0

    for i in range(1, n + 1):
        xor1 ^= i

    for num in arr:
        xor2 ^= num

    return xor1 ^ xor2


# -------------------------------
# Driver Code
# -------------------------------
arr = [1, 2, 4, 5]
n = 5

print("Brute Force :", brute(arr, n))
print("Hashing     :", hashing(arr, n))
print("Sum Formula :", sum_formula(arr, n))
print("XOR         :", xor_method(arr, n))