class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        res=0
        for num in nums:
            if num!=val:
                nums[res]=num
                res+=1
        return res