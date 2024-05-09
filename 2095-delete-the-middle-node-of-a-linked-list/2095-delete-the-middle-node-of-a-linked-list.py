# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None
        slowP = head
        fastP = head
        prev = None
        while fastP and fastP.next:
            prev = slowP
            slowP = slowP.next
            fastP = fastP.next.next
        #slowP is at middle
        prev.next = slowP.next
        return head



        