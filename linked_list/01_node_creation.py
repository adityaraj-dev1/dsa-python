# Singly Linked List - Node Creation


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)


# Connecting nodes
node1.next = node2
node2.next = node3


# Head points to the first node
head = node1


# Linked List:
# 10 → 20 → 30 → None


print(head.data)
print(head.next.data)
print(head.next.next.data)