# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def divide(self, head):
        if head is None:
            return head

        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):  
       
        newNode = ListNode()
        temp = newNode
        while left and right:
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        if left is not None:
            temp.next = left
        if right is not None:
            temp.next = right

        head = newNode.next
        return head

    def sortList(self, head):
        if head is None or head.next is None:
            return head

        middle = self.divide(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.sortList(head)
        right = self.sortList(next_to_middle)
        sorted_list = self.merge(left, right)
        return sorted_list

    
        
        