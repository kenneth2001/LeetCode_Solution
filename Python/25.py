# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        p = head
        for _ in range(k):
            if not p:
                return head
            p = p.next
        new_head = self.reverseKGroup(p, k)
        p = head
        for _ in range(k):
            q = p.next
            p.next = new_head
            new_head = p
            p = q
        return new_head
