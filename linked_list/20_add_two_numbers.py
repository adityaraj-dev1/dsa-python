class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def add_two_numbers(head1, head2):
    dummy = Node(0)
    current = dummy

    current1 = head1
    current2 = head2
    carry = 0

    while current1 is not None or current2 is not None:

        value1 = current1.data if current1 is not None else 0
        value2 = current2.data if current2 is not None else 0

        total = value1 + value2 + carry

        digit = total % 10
        carry = total // 10

        current.next = Node(digit)
        current = current.next

        if current1 is not None:
            current1 = current1.next

        if current2 is not None:
            current2 = current2.next

    if carry != 0:
        current.next = Node(carry)

    return dummy.next


# Example:
# 342 + 465 = 807
head1 = Node(2)
head1.next = Node(4)
head1.next.next = Node(3)

head2 = Node(5)
head2.next = Node(6)
head2.next.next = Node(4)

result = add_two_numbers(head1, head2)

current = result
while current is not None:
    print(current.data, end=" ")
    current = current.next