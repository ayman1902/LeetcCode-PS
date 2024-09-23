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
        lenght=0
        lenght_arr=[]
        j=0
        for i in range(n):
            if nums[i]-1 not in nums_set:
                while nums[i]+j in nums_set:
                    j+=1
                    lenght+=1
                lenght_arr.append(lenght)
                lenght=0
                j=0
        return max(lenght_arr)