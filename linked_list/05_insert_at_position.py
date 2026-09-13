# Singly Linked List - Insertion at Given Position


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1


# Insert at a given position
def insert_at_position(head, data, position):

    new_node = Node(data)

    # If position is 0,
    # insert at the beginning
    if position == 0:
        new_node.next = head
        return new_node

    current = head

    # Move to the node before the position
    for i in range(position - 1):
        current = current.next

    # Connect new node
    new_node.next = current.next
    current.next = new_node

    return head


# Insert 15 at position 2
head = insert_at_position(head, 15, 2)


# Print list
current = head

while current is not None:
    print(current.data)
    current = current.next


# Time Complexity: O(n)
# Space Complexity: O(1)