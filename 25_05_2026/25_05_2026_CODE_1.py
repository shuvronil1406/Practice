#LC 19. Remove Nth Node From End of List
#CODE:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp is not None:
            count +=1
            temp = temp.next
        if count == n:
            # head.val = None -->this wont return [], rather it will return None
            return head.next    #--> this returns []
        # index = 0
        ptr = head
        for i in range(count - n -1):
            ptr = ptr.next
            # index +=1
        ptr.next = ptr.next.next
        return head






        