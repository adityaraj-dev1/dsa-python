class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)


# Connect nodes
node1.next = node2
node1.prev = None

node2.next = node3
node2.prev = node1

node3.next = None
node3.prev = node2


head = node1


def count_nodes(head):
    current = head
    count = 0

    while current is not None:
        count += 1
        current = current.next

    return count


print("Number of nodes:", count_nodes(head))


# Time Complexity: O(n)
# Space Complexity: O(1)