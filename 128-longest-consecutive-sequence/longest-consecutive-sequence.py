class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==0:
            return 0
        nums_set=set(nums)
        longest=0
        j=0
        for i in range(n):
            if nums[i]-1 not in nums_set:
                lenght=0
                while nums[i]+j in nums_set:
                    j+=1
                    lenght+=1
                longest=max(longest,lenght)
                j=0
        return longest