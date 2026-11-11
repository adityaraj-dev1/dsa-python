"""
Problem: Remove All Adjacent Duplicates in String
LeetCode: 1047
Difficulty: Easy

Approach: Stack

Time Complexity: O(n)
Space Complexity: O(n)
"""

def removeduplicates(s):
    stack = []
    for ch in s:
        if not stack or stack[-1] != ch:
            stack.append(ch)
        else:
            stack.pop()
    return "".join(stack)            