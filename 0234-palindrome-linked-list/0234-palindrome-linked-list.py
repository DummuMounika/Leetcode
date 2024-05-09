# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        newhead = self.reverseList(head.next)
        nextNode = head.next
        nextNode.next = head
        head.next = None
        return newhead
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        slowP = head
        fastP = head
        while fastP.next and fastP.next.next:
            slowP = slowP.next
            fastP = fastP.next.next
        newhead = self.reverseList(slowP.next)
        first = head
        second = newhead
        while second:
            if second.val != first.val:
                return False
            second = second.next
            first = first.next
        return True
        

        