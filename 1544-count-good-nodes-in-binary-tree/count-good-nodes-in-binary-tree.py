# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node,max_value):
            res=0
            if node == None:
                return 0
            if node.val >= max_value:
                res+=1
            max_value=max(node.val,max_value)
            res+=dfs(node.left,max_value)
            res+=dfs(node.right,max_value)
            return res
        return dfs(root,root.val)
        