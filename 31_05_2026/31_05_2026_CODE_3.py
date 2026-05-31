#21. Merge Two Sorted Lists
#CODE:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = list1
        r = list2
        res=[]
        while l is not None and r is not None:
            if l.val <= r.val:
                res.append(l.val)
                l = l.next
            else:
                res.append(r.val)
                r = r.next
        while l is not None:
            res.append(l.val)
            l = l.next
        while r is not None:
            res.append(r.val)
            r=r.next
        result = ListNode()
        ptr = result
        for i in res:
            ptr.next = ListNode(i) # creates a new node and connects it to the previous node
            ptr = ptr.next
        return result.next #since the first nodes value is 0, so we return result.next
    
        