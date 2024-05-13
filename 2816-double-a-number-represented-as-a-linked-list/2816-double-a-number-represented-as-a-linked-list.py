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

    def doubleIt(self, head):
        # Reverse the linked list
        head = self.reverseLL(head)

        NewList = ListNode(0) #0 -> 8 -> 9 ->9 ->1
        temp = NewList 
        carry = 0
        while head is not None or carry != 0:
            temp1= head.val if head else 0 
            #sum + count
            total = temp1 * 2 + carry 
            carry = total//10 

            #create a newnode with this sum
            temp.next = ListNode(total%10) 
            temp = temp.next

            head=head.next  if head else None    

        NewList = NewList.next
        # Reverse the linked list
        head = self.reverseLL(NewList)
        
        return head



        