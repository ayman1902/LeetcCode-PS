class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binarysearch(start,finish):
            if start==finish:
                return start
            mid=(start+finish)//2
            if nums[mid]>nums[mid+1]:
                return binarysearch(start,mid)
            else:
                return binarysearch(mid+1,finish)
        return binarysearch(0,len(nums)-1)