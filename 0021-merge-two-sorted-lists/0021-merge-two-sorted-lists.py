# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        newList = ListNode(0)
        temp = newList
        l1 = list1
        l2 = list2
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1 is not None:
            temp.next = l1
        elif l2 is not None:
            temp.next = l2  
             
        return newList.next



        