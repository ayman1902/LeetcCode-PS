class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap=defaultdict(int)
        comb=0
        for i in range(len(nums)):
            comb=target-nums[i]
            if comb in hashmap:
                return [hashmap[comb],i]
            hashmap[nums[i]]=i
            