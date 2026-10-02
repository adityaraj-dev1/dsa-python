class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connect nodes
node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3

head = node1


def reverse(head):
    current = head

    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp

        if current.prev is None:
            head = current
            break

        current = current.prev

    return head


head = reverse(head)

# Forward traversal
current = head
while current is not None:
    print(current.data, end=" <-> ")
    current = current.next

print("None")

# Time Complexity: O(n)
# Space Complexity: O(1)