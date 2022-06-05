def reverse(head):
    if not head.next:
        return head
    p,c,n = head, head.next, head.next.next

    p.next = None

    while n:
        c.next = p
        p, c, n = c, n, n.next
    c.next = p
    return c 
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        head = reverse(head)
        return(head)