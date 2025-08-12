# Last updated: 8/11/2025, 10:47:41 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        def recursive(branch_p, branch_q):
            if branch_p == None and branch_q == None:
                return True
            if branch_p == None or branch_q == None:
                return False
            if branch_p.val == branch_q.val:
                return (recursive(branch_p.right, branch_q.right) and recursive(branch_p.left, branch_q.left))
            else:
                return False

        return recursive(p, q)

        