"""
Problem: Armstrong Number

Approach:
Count the number of digits and raise each digit to the power
of the total number of digits.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def armstrong(num):
    if num == 0:
        return True

    count = 0
    temp = num

    while temp > 0:
        count += 1
        temp //= 10

    total = 0
    original = num

    while num > 0:
        last = num % 10
        total += last ** count
        num //= 10

    return total == original


num = int(input("Enter a number: "))
print("Armstrong Number:", armstrong(num))
