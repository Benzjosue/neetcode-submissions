# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []

        current = head

        while current:

            stack.append(current)
            current = current.next

        if stack:
        
            head = stack.pop()
            current = head


            while stack:
                current.next = stack.pop()
                print(current.val)
                current = current.next

            current.next = None
                

            return head





        


        