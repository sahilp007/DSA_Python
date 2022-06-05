class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


head = Node("Phase1", Node("Phase2", Node("Phase3", None)))


def print_LL(head):
    while head:
        print(head.data)
        head = head.next


def insert_last(head, data):
    n = Node(data, None)
    if not head:
        return n
    p = head
    while p.next:
        p = p.next
    p.next = n
    return head


def insert_first(head, data):
    n = Node(data, None)
    n.next = head
    return n


head = insert_last(head, 4)
head = insert_first(head, "hoi")
print_LL(head)
