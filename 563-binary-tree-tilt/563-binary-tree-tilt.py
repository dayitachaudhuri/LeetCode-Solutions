# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        count=[0]
        def helper(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return root.val
            left=helper(root.left)
            right=helper(root.right)
            count[0]+=abs(left-right)
            return root.val+left+right
        helper(root)
        return count[0]