# Last updated: 8/10/2025, 10:22:04 PM
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
        temp1 = list1
        temp2 = list2
        if temp1 == None and temp2 == None:
            return None
        if temp1 == None:
            return temp2
        if temp2 == None:
            return temp1
        if temp1.val > temp2.val:
            result = ListNode(temp2.val)
            temp2 = temp2.next
        else:
            result = ListNode(temp1.val)
            temp1 = temp1.next

        tempresult = result
        while temp1 != None or temp2 != None:
            if temp1 == None:
                tempresult.next = ListNode(temp2.val)
                tempresult = tempresult.next
                temp2 = temp2.next
                continue
            elif temp2 == None:
                tempresult.next = ListNode(temp1.val)
                tempresult = tempresult.next
                temp1 = temp1.next
                continue
            print(temp1.val, temp2.val)
            if temp1.val > temp2.val:
                tempresult.next = ListNode(temp2.val)
                tempresult = tempresult.next
                temp2 = temp2.next
                continue
            else:
                tempresult.next = ListNode(temp1.val)
                tempresult = tempresult.next
                temp1 = temp1.next
                continue

        return result

            
        
            



        