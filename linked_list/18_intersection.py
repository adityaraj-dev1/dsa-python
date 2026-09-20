class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def intersection(head1, head2):
    p1 = head1
    p2 = head2

    while p1 != p2:
        if p1 is None:
            p1 = head2
        else:
            p1 = p1.next

        if p2 is None:
            p2 = head1
        else:
            p2 = p2.next

    return p1


# Example
common1 = Node(8)
common2 = Node(10)

common1.next = common2

node1 = Node(1)
node2 = Node(2)

node1.next = node2
node2.next = common1

node3 = Node(3)
node4 = Node(4)

node3.next = node4
node4.next = common1

head1 = node1
head2 = node3

result = intersection(head1, head2)

if result is not None:
    print("Intersection:", result.data)
else:
    print("No intersection")


# Time Complexity: O(n + m)
# Space Complexity: O(1)