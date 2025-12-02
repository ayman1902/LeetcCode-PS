"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        res=1
        if not root:
            return 0
        if not root.children :
            return 1
        for node in root.children:
            res=max(res,self.maxDepth(node)+1)
        return res
        