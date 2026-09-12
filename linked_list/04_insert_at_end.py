# Singly Linked List - Insertion at End


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


# Insert at end
def insert_at_end(head, data):

    new_node = Node(data)

    current = head

    while current.next is not None:
        current = current.next

    current.next = new_node

    return head


# Insert 40
head = insert_at_end(head, 40)


# Print list
current = head

while current is not None:
    print(current.data)
    current = current.next


# Time Complexity: O(n)
# Space Complexity: O(1)