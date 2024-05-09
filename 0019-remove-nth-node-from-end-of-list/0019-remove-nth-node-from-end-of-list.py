# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        indexNode = head
        length = 0
        while indexNode:
            indexNode = indexNode.next
            length = length + 1
        if length == n:
            return head.next
        indexNode = head
        for i in range(1, length - n):
            indexNode = indexNode.next
        indexNode.next = indexNode.next.next
        return head
        


        