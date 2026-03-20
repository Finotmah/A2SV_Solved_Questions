# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findsmall(node):
            while node.left:
                node = node.left
            return node
        
        if not root:
            return None
        elif key < root.val:
           root.left =  self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                next_bigger = findsmall(root.right)
                root.val = next_bigger.val
                root.right = self.deleteNode(root.right,next_bigger.val)

        return root


                


                
