# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if  head is None:
            return None
        
        dummy = ListNode(0)
        dummy.next = head

        current = head
        prev = dummy

        while  current is not None and current.next is not None :
            if current.val == current.next.val:
                while current.next is not None and current.val == current.next.val:
                    current = current.next
                current = current.next
                prev.next = current
            else:  
                prev = current
                current = current.next  

        return dummy.next

        