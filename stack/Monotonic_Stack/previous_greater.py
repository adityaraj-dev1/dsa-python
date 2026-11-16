"""
Problem: Previous Greater Element
Approach: Monotonic Decreasing Stack

Time Complexity: O(n)
Space Complexity: O(n)
"""

def previous_greater(arr):
    stack = []
    result = []

    for x in arr:

        while stack and stack[-1] <= x:
            stack.pop()

        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

        stack.append(x)

    return result


arr = [4, 5, 2, 10, 8]
print(previous_greater(arr))