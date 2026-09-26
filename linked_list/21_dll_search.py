class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node1.prev = None

node2.next = node3
node2.prev = node1

node3.next = None
node3.prev = node2

head = node1


def search(head, element):
    current = head

    while current is not None:
        if current.data == element:
            return True

        current = current.next

    return False


print(search(head, 20))


# Time Complexity: O(n)
# Space Complexity: O(1)