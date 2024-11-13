class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        hashMap={}
        s=set()
        for i in range(len(nums)):
            hashMap[nums[i]]=i
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                disered=-nums[i]-nums[j]
                if(disered in hashMap and hashMap[disered]!=i and hashMap[disered]!=j):
                    s.add(tuple(sorted([disered,nums[i],nums[j]])))
        print(hashMap,s)
        res=[]
        for e in s:
            res.append(list(e))
            print(list(e))
        return res

        