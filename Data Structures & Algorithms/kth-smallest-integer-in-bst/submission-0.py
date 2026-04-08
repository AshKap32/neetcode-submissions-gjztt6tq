# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Inorder Travesal up kth 

        int_k = k
        res = root.val

        def inorderKth(root):
            nonlocal int_k, res
            if not root: 
                return
            
            inorderKth(root.left)
            int_k -= 1
            if int_k == 0: 
                res = root.val
                return 
            inorderKth(root.right)

        inorderKth(root)
        return res
