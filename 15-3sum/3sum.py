class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        res=[]
        for k in range(n):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i=k+1
            j=n-1
            while i<j:
                combin=nums[k]+nums[i]+nums[j]
                if combin==0:
                    res.append([nums[k],nums[i],nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif combin>0:
                    j-=1
                else:
                    i+=1
        return res


        