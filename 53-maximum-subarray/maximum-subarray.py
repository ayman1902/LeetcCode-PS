class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        subsequence=[nums[0]]
        current_sum=nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):
            if current_sum + nums[i] > nums[i]:
                current_sum+=nums[i]
                subsequence.append(nums[i])
            else:
                current_sum=nums[i]
                subsequence=[nums[i]]
            if current_sum > max_sum:
                max_sum=current_sum
        return max_sum
            

        