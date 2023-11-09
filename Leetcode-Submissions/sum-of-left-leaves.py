# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(node,dxn=''):

            if not node:
                return 0

            if( not node.left and not node.right and dxn=='L'):
                return node.val

            return dfs(node.left,'L')+dfs(node.right,'R')


        return dfs(root)
        