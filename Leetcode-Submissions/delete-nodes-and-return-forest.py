# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        to_delete = set(to_delete)
        answer = set()
        def dfs(curr_node,prev=TreeNode(),dxn='',added=False):

            if(curr_node==None):
                return 

            if(curr_node.val not in to_delete and not added):

                answer.add(curr_node)
                added=True

            elif(curr_node.val in to_delete):
                added=False
                if(dxn=='L'):
                    prev.left=None
                else:
                    prev.right = None

            dfs(curr_node.left,curr_node,'L',added)
            dfs(curr_node.right,curr_node,'R',added)

        dfs(root)

        return list(answer)