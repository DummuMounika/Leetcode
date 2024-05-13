# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseLL(self,head):
        current = head
        prev = None
        while current is not None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        head = prev
        return head
        
    def removeNodes(self, head):
        if not head:
            return None
        
        #Reverse Linkedlist
        head = self.reverseLL(head)

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

        #Reverse Linkedlist
        head = self.reverseLL(head)
        return head




        