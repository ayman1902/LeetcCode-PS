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
        for item in nums_set:
            if item-1 not in nums_set:
                lenght=1
                while item+lenght in nums_set:
                    lenght+=1
                longest=max(longest,lenght)
        return longest