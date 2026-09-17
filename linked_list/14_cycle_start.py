class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def cycle_start(head):
    slow = head
    fast = head

    # Phase 1: Detect cycle
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Phase 2: Find cycle starting node
            entry = head

            while entry != slow:
                entry = entry.next
                slow = slow.next

            return entry

    return None


# Example
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node3

head = node1

result = cycle_start(head)

if result is not None:
    print(result.data)
else:
    print("No cycle")

# Time Complexity: O(n)
# Space Complexity: O(1)