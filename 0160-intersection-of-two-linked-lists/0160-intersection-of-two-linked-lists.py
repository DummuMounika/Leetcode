# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        L1 = headA
        L2 = headB
        while L1 != L2:
            if L1 is not None :
                L1 = L1.next
            else:
                L1 = headB
            
            if L2 is not None :
                L2 = L2.next
            else:
                L2 = headA
            
        return L1
            
        