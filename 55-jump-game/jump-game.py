class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest=0
        for i in range(len(nums)):
            if i > furthest:
                return False
            furthest=max(furthest,i+nums[i])
        return True
        
            