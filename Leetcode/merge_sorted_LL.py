

head = ans = ListNode(0)
while l1 and l2:
    if l1.data<=l2.data:
        ans.next = l1
        l1 = l1.next
        ans = ans.next
    elif l2.data<=l1.data:
        ans.next = l2
        l2 = l2.next
        ans = ans.next
ans.next = l1 or l2
return head.next