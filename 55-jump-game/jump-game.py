class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest=0
        for i in range(len(nums)):
            if i > furthest:#ila kan aslan rak mat9derch twssel l index so false
                return False
            furthest=max(furthest,i+nums[i])#update il kan matupdati assat
        return True
        
            