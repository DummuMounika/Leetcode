# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None
        currentNode = head
        while currentNode and currentNode.next is not None:
            if currentNode.val == currentNode.next.val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        return head
        