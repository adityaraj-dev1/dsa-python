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

node2.prev = node1
node2.next = node3

node3.prev = node2

head = node1
tail = node3


def insert_at_beginning(head, tail, element):
    new_node = Node(element)

    # Empty list
    if head is None:
        head = new_node
        tail = new_node
        return head, tail

    new_node.next = head
    head.prev = new_node
    head = new_node

    return head, tail


head, tail = insert_at_beginning(head, tail, 5)


# Forward traversal
current = head
while current is not None:
    print(current.data, end=" <-> ")
    current = current.next

print("None")


# Time Complexity: O(1)
# Space Complexity: O(1)