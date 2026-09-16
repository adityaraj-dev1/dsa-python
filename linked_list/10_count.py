class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def count_nodes(head):
    count = 0
    current = head

    while current is not None:
        count += 1
        current = current.next

    return count


# Example
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1

print(count_nodes(head))

# Time Complexity: O(n)
# Space Complexity: O(1)