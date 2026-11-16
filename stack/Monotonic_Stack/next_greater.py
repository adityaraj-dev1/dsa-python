"""
Problem: Next Greater Element
Approach: Monotonic Decreasing Stack

Description:
Find the nearest greater element on the right
for every element in the array.
Return -1 if no greater element exists.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def nextgreater(arr):
    stack = []
    result = []

    # Traverse from right to left
    for i in range(len(arr) - 1, -1, -1):

        # Remove smaller or equal elements
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # Find next greater element
        if stack:
            result.append(stack[-1])
        else:
            result.append(-1)

        # Push current element
        stack.append(arr[i])

    # Reverse result to restore original order
    return result[::-1]


arr = [6, 3, 8, 4, 9]
print(nextgreater(arr))