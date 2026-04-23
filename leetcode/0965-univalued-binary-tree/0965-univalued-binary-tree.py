# Definition for a binary tree vertex.
# class Treevertex:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isUnivalTree(self, root: Optional[Treevertex]) -> bool:
        queue = deque([root])
        while queue:
            vertex = queue.popleft()
            if vertex.val != root.val:
                return False
            if vertex.left:
                queue.append(vertex.left)
            if vertex.right:
                queue.append(vertex.right)
        return True