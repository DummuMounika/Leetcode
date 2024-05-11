# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode] 
        8 -> 13
        """
        if not head:
            return None

        current = head
        prev = None
        while current is not None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        head = prev

        # 8 -> 3 -> 13 -> 2 -> 5
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next is not None and current.next.next is not None:
            if current.val > current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        if current.next is not None and current.val > current.next.val:
            current.next = None

        prev = None
        while head is not None:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode

        return prev




        