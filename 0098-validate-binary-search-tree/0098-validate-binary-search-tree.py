# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root,low,high):
            if root is None:
                return True
            if (low < root.val and high > root.val):
                return valid(root.left,low,root.val) and valid(root.right,root.val,high)
            else:
                return False
        return valid(root,float("-inf"),float("inf"))
        