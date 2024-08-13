class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap=defaultdict(int)
        n=len(nums)
        for i in range(n):
            hashmap[nums[i]]+=1
        for key,value in hashmap.items():
            if value>n//2:
                print(key,value)
                return key
