# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        # Circular Linkedlist
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head

        t = length - k % length
        for _ in range(length - k % length):
            tail = tail.next
        newHead = tail.next
        tail.next = None
        return newHead
    