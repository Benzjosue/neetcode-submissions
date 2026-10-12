# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []
        current = head
        original = head



        while current:
            stack.append(current)
            current = current.next

        if not stack:
            return None

        new_head = stack.pop()
        current = new_head
       

        while stack:
            
            current.next = stack.pop()
            current = current.next

        current.next = None


        return new_head


        






        


        