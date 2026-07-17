"""
Problem: Reverse Integer

Approach:
Reverse the number using modulo (%) and integer division (//).
Handle negative numbers and check for 32-bit integer overflow.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def reverse(num):
    reversed_num = 0

    if num < 0:
        sign = -1
    else:
        sign = 1

    num = abs(num)

    while num > 0:
        last = num % 10
        reversed_num = (reversed_num * 10) + last
        num //= 10

    reversed_num *= sign

    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0

    return reversed_num


num = int(input("Enter a number: "))
print("Reversed number:", reverse(num))
