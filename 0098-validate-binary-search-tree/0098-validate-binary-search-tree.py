# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        def test1(root1: Optional[TreeNode]):
            if root1 == None:
                return 0
            ri = root1.right
            if ri == None:
                return root1.val
            return test1(ri)
            
        def test2(root2 : Optional[TreeNode]):
            if root2 == None:
                return 0
            ri = root2.left
            if ri == None:
                return root2.val
            return test2(ri)  

        lefty = root.left
        righty = root.right 
            
        if self.isValidBST(lefty) and self.isValidBST(righty):
            if (lefty == None or test1(lefty) < root.val) and ( righty == None or  test2(righty) > root.val):
                return True
        return False
            

        
        