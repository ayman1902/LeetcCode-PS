class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=0
        j=len(nums)-1
        res=0
        nums.sort()
        while i<j:
            if nums[i]+nums[j]==k:
                res+=1
                i+=1
                j-=1
            elif k-nums[i]>nums[j]:
                i+=1
            else:
                j-=1
        return res
        