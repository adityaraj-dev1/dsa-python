class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


# Example
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1

head = reverse(head)

current = head
while current is not None:
    print(current.data)
    current = current.next

# Time Complexity: O(n)
# Space Complexity: O(1)