# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def sumOfNoneVal(node,parent,grand):
            if not node:
                return 0
            total = 0
            if grand and grand.val%2 == 0:
                total += node.val
            total += sumOfNoneVal(node.left, node, parent)
            total += sumOfNoneVal(node.right, node, parent)
            return total
        
        return sumOfNoneVal(root,None,None)