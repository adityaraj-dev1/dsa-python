class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_at_position(head, position):
    
    if head is None:
        return None

    if position == 0:
        return head.next

    current = head

    for i in range(position - 1):
        current = current.next

    current.next = current.next.next

    return head


# Example
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1

head = delete_at_position(head, 1)

current = head
while current is not None:
    print(current.data)
    current = current.next

# Time Complexity: O(n)
# Space Complexity: O(1)
