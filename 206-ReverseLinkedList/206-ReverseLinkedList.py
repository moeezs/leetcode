# Last updated: 8/9/2025, 10:05:30 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None or head.next == None:
            return head
        ret = ListNode(head.val)

        while head.next != None:
            head = head.next
            temp = ListNode(head.val)
            temp.next = ret
            ret = temp
            

        return ret

        