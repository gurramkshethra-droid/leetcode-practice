# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp=ListNode(0)
        t=temp
        min=0
        while list1 and list2:
            if(list1.val<=list2.val):
                t.next=list1
                list1=list1.next
            else:
                t.next=list2
                list2=list2.next  
            t=t.next
        if list1:
            t.next=list1
        if list2:
            t.next=list2
        return temp.next
        