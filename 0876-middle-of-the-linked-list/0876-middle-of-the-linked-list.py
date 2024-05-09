# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slowP = head
        fastP = head
        while (fastP != None and fastP.next != None):
            slowP = slowP.next
            fastP = fastP.next.next
        return slowP




        