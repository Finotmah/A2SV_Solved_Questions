# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        def solve(node,c_sum):
            if not node:
                return 0
            c_sum += node.val
            count = prefix_sum[c_sum - targetSum]
            prefix_sum[c_sum] += 1

            count += solve(node.left,c_sum)
            count += solve(node.right,c_sum)

            prefix_sum[c_sum] -= 1

            return count
        return solve(root,0)