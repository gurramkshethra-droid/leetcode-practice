# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        i=0
        temp= ListNode(0)
        temp.next =head
        f=temp
        s=temp
        while(i<n):
            f=f.next
            i+=1
        while f.next:
            f=f.next
            s=s.next
        s.next=s.next.next
        return temp.next

        