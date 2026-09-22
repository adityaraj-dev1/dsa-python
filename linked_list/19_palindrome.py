class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def palindrome(head):
    if head is None or head.next is None:
        return True

    slow = head
    fast = head

    # Find middle
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    current = slow
    previous = None

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    second_half = previous

    # Compare both halves
    first = head
    second = second_half

    while second is not None:
        if first.data != second.data:
            return False

        first = first.next
        second = second.next

    return True


# Example
node1 = Node(1)
node2 = Node(2)
node3 = Node(2)
node4 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

print(palindrome(head))


# Time Complexity: O(n)
# Space Complexity: O(1)