"""
Problem:
Count the number of digits in a given integer.

Approach:
Repeatedly remove the last digit using integer division (// 10)
and count how many times this operation is performed.

Time Complexity: O(log₁₀ n)
Space Complexity: O(1)
"""

def count_digits(num):
    # Edge case: 0 has one digit
    if num == 0:
        return 1

    # Handle negative numbers
    num = abs(num)

    count = 0

    while num > 0:
        count += 1
        num //= 10

    return count


# Driver Code
num = int(input("Enter a number: "))
print("Number of digits:", count_digits(num))
