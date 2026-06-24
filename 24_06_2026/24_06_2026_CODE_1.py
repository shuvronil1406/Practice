#LC 234. Palindrome Linked List
#CODE:

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        L=[]
        while temp is not None:
            L.append(temp.val)
            temp = temp.next
        return L == L[::-1]