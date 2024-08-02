# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_zig_zag=0
        def dfs(node, direction, length):
            if node == None:
                return
            self.max_zig_zag=max(self.max_zig_zag,length)
            if direction ==0:#left
                dfs(node.left,1,length+1)
                dfs(node.right,0,1)
            elif direction ==1:#right
                dfs(node.right,0,length+1)
                dfs(node.left,1,1)
        dfs(root,0,0)
        dfs(root,1,0)
        return self.max_zig_zag
                
            
