# Singly Linked List - Insertion at Beginning


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


# Insert at beginning
def insert_at_beginning(head, data):

    new_node = Node(data)

    new_node.next = head

    head = new_node

    return head


# Insert 5
head = insert_at_beginning(head, 5)


# Print list
current = head

while current is not None:
    print(current.data)
    current = current.next


# Time Complexity: O(1)
# Space Complexity: O(1)