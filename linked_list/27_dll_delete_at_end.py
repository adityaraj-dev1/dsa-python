class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2

head = node1
tail = node3


def delete_at_end(head, tail):
    if head is None:
        return None, None

    if head == tail:
        return None, None

    tail = tail.prev
    tail.next = None

    return head, tail


head, tail = delete_at_end(head, tail)


current = head
while current is not None:
    print(current.data, end=" <-> ")
    current = current.next

print("None")


# Time Complexity: O(1)
# Space Complexity: O(1)