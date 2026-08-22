# Square Root of a Number

# Brute Force
def square_root_brute(num):
    ans = 0

    for i in range(num + 1):
        if i * i <= num:
            ans = i
        else:
            break

    return ans


# Optimal - Binary Search
def square_root(num):
    left = 0
    right = num
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid <= num:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans


num = 27

print(square_root_brute(num))  # 5
print(square_root(num))        # 5


# Brute Force:
# Time Complexity: O(n)
# Space Complexity: O(1)

# Optimal:
# Time Complexity: O(log n)
# Space Complexity: O(1)