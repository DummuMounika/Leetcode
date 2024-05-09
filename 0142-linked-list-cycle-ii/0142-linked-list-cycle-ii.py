# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slowP = head
        fastP = head
        while fastP and fastP.next :
            slowP = slowP.next
            fastP = fastP.next.next
            if fastP == slowP:
                slowP = head
                while slowP != fastP:
                    slowP = slowP.next
                    fastP = fastP.next
                return slowP
        return None
        