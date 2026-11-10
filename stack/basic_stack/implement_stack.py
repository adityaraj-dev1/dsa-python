"""
Problem: Implement Stack using Python Class

Time Complexity:
push()     : O(1)
pop()      : O(1)
top()      : O(1)
isEmpty()  : O(1)
size()     : O(1)

Space Complexity: O(n)
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack.pop()

    def top(self):
        if not self.stack:
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)