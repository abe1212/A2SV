# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        curr_node = root
        prev=None
        while(curr_node):
            if(curr_node.val == key):
                break
            elif(key > curr_node.val):
                prev=curr_node
                curr_node=curr_node.right
            else:
                prev=curr_node
                curr_node=curr_node.left


        if(not curr_node):
            return root
        elif(not curr_node.left or not curr_node.right):
            
            child = None
            if(not curr_node.left):
                child = curr_node.right
            elif(not curr_node.right):
                child = curr_node.left

            if(prev and curr_node.val >= prev.val):
                prev.right=child
            elif(prev):
                prev.left=child
            else:
                return child
        
        else:
            smallest = self.get_smallest(curr_node.right)
            # print('smallest',smallest,'root',root,'current ',curr_node)
            curr_node.val = smallest.val
            curr_node.right = self.deleteNode(curr_node.right,smallest.val)

        return root


    def get_smallest(self,root):
        
        curr = root
        while(curr.left):
            curr=curr.left
        return curr

        

