class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res=[]
        n=len(nums)
        if n==0:
            return []
        
        start=nums[0]
        finish=nums[0]
        
        def construct(a, b):
            if a == b:
                return str(a)
            else:
                return str(a) + "->" + str(b)
        for i in range(1,n):
            if nums[i] != nums[i-1]+1:
                res.append(construct(start,finish))
                start=nums[i]
                finish=nums[i]
            else:
                finish=nums[i]
        res.append(construct(start,finish))

        return res
        