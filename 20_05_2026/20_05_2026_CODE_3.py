#LC 148. Sort List

#CODE: 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        arr=[]
        while temp is not None:
            arr.append(temp.val)
            temp = temp.next
        sorted_arr = sorted(arr)
        temp2 = head
        i=0
        while temp2 is not None:
            temp2.val = sorted_arr[i]
            temp2=temp2.next
            i+=1
        return head
