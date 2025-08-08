# Last updated: 8/8/2025, 10:02:44 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp1 = l1
        l1s = ''
        while temp1 != None:
            l1s += str(temp1.val)
            temp1 = temp1.next


        temp2 = l2
        l2s = ''
        while temp2 != None:
            l2s += str(temp2.val)
            temp2 = temp2.next


        answer = str(int(l1s[::-1]) + int (l2s[::-1]))
        answer = answer[::-1]

        result = ListNode(int(answer[0]))
        tempresult = result
        for i in range(1, len(answer)):
            tempresult.next = ListNode(int(answer[i]))
            tempresult = tempresult.next
        print(tempresult)
        
        return result



        