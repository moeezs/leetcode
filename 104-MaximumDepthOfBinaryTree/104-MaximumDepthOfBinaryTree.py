# Last updated: 12/28/2025, 6:31:30 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def recursive(branch):
            if branch == None:
                return 0
            else:
                return 1 + max(recursive(branch.left), recursive(branch.right))
            
        return recursive(root)


        