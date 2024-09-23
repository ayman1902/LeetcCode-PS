class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        nums_set=set(nums)
        lenght=0
        lenght_arr=[]
        j=0
        for i in range(len(nums)):
            if nums[i]-1 in nums_set:
                continue
            else:
                while nums[i]+j in nums_set:
                    j+=1
                    lenght+=1
                lenght_arr.append(lenght)
                lenght=0
                j=0
        return max(lenght_arr)