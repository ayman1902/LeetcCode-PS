class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pointer1=float('inf')
        pointer2=float('inf')
        for i in range(len(nums)):
            if nums[i]<=pointer1:
                pointer1=nums[i]
            elif nums[i]<=pointer2:
                pointer2=nums[i]
            else:
                return True
        return False

        