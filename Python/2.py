# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        newNode = ListNode(0)
        currentNode = newNode
        carry = 0
        while l1  or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry = val // 10
            currentNode.next = ListNode(val % 10)
            currentNode = currentNode.next
            
        if carry == 1:
            currentNode.next = ListNode(1)
        return newNode.next
