class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


# Example
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1

print(find_middle(head).data)

# Time Complexity: O(n)
# Space Complexity: O(1)