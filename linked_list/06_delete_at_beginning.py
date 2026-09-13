class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_at_beginning(head):

    if head is None:
        return None

    head = head.next
    return head


# Example
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1

head = delete_at_beginning(head)

current = head
while current is not None:
    print(current.data)
    current = current.next

 # Time Complexity: O(1)
 # Space Complexity: O(1)    