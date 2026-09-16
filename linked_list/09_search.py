class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def search(head, value):
    current = head

    while current is not None:
        if current.data == value:
            return True
        current = current.next

    return False


# Example
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1

print(search(head, 20))

# Time Complexity: O(n)
# Space Complexity: O(1)