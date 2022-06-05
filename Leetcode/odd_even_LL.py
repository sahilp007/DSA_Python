def eo(head):
    if head:
        odd = head
        even = evenHead = odd.next
        while even and even.next:
            odd.next = odd = even.next
            even.next = even = odd.next
        odd.next = evenHead
    return head