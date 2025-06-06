# Last updated: 05/06/2025, 22:14:12
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1 = ''
        current_1 = l1
        while current_1:
            num_1 += str(current_1.val)
            current_1 = current_1.next

        num_2 = ''
        current_2 = l2
        while current_2:
            num_2 += str(current_2.val)
            current_2 = current_2.next

        num_1 = num_1[::-1]
        num_2 = num_2[::-1]

        sum = str(int(num_1) + int(num_2))
        sum = sum[::-1]

        chars = []

        for i in range(len(sum)):
            chars.append(sum[i])

        dummy = ListNode()
        current = dummy
        for char in chars:
            current.next = ListNode(int(char))
            current = current.next

        return dummy.next