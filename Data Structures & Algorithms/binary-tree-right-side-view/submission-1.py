# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()   
        res = []

        if root: 
            queue.append(root)
        
        while len(queue) > 0:
            r_val = None
            for i in range(len(queue)):
                curr = queue.popleft()
                r_val = curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(r_val)
        return res
                
            