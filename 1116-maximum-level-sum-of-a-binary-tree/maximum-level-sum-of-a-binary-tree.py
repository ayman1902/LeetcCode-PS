# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not (root.left or root.right):
            return 1
        queue=[root]
        max=float("-inf")
        res=0
        level=0
        while queue:
            level+=1
            level_size=len(queue)
            level_value=[]
            for i in range(level_size):
                value_level=queue.pop(0)
                level_value.append(value_level.val)
    
                if value_level.left:
                    queue.append(value_level.left)
                if value_level.right:
                    queue.append(value_level.right)
            if sum(level_value)>max:
                max=sum(level_value)
                res=level
        return res


        