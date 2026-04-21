# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def dfs(node):
            nonlocal max_sum
            if not node:
                return True, 0, float('inf'), float('-inf')
            l_bst, l_sum, l_min, l_max = dfs(node.left)
            r_bst, r_sum, r_min, r_max = dfs(node.right)

            if l_bst and r_bst and l_max < node.val < r_min:
                curr_sum = l_sum + r_sum + node.val
                max_sum = max(max_sum, curr_sum)
                
                return True, curr_sum, min(l_min, node.val), max(r_max, node.val)
            
            return False, 0, 0, 0
        dfs(root)
        return max_sum