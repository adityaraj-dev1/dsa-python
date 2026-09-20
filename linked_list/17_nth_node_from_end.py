class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def nth_node_from_end(head, n):
    dummy = Node(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next


# Example
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

head = nth_node_from_end(head, 2)

current = head
while current is not None:
    print(current.data)
    current = current.next


# Time Complexity: O(n)
# Space Complexity: O(1)