# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        ###Iterative Method###
        # curr = head
        # prev = None
        # while not curr is None:
        #     nextNode = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nextNode
        # head = prev;    
        # return head

        #Recursive Method
        
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        nextNode = head.next
        nextNode.next = head
        head.next = None
        return new_head
        