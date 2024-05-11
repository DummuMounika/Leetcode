# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for i in range(left-1):
            prev = prev.next
        
        rev = None
        curr = prev.next

        for i in range(right - left+1):
                nextNode = curr.next
                curr.next = rev
                rev = curr
                curr = nextNode  

        prev.next.next = curr
        prev.next = rev
        return dummy.next
        