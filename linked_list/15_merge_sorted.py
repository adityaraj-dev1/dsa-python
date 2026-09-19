class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_sorted(head1, head2):
    dummy = Node(0)
    current = dummy

    current1 = head1
    current2 = head2

    while current1 is not None and current2 is not None:
        if current1.data < current2.data:
            current.next = current1
            current1 = current1.next
        else:
            current.next = current2
            current2 = current2.next

        current = current.next

    current.next = current1 if current1 is not None else current2

    return dummy.next


# Example
node1 = Node(1)
node2 = Node(3)
node3 = Node(5)

node1.next = node2
node2.next = node3

node4 = Node(2)
node5 = Node(4)
node6 = Node(6)

node4.next = node5
node5.next = node6

head1 = node1
head2 = node4

head = merge_sorted(head1, head2)

current = head
while current is not None:
    print(current.data)
    current = current.next


# Time Complexity: O(n + m)
# Space Complexity: O(1)