# Last updated: 8/10/2025, 10:47:30 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def recursive(branch):
            if branch == None:
                return branch
            else:
                temp = TreeNode(branch.val)
                temp.left = recursive(branch.right)
                temp.right = recursive(branch.left)
                return temp
        if root == None:
            return None
        return recursive(root)
        