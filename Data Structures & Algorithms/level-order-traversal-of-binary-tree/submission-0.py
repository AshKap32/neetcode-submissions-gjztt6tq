# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        bfs_list = []

        if root:
            queue.append(root)
        
        while len(queue) > 0:

            level_list = []

            for i in range(len(queue)):
                curr = queue.popleft()
                level_list.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            bfs_list.append(level_list)
            level_list = []


        return bfs_list