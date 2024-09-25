class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap=defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]]+=1
            if hashmap[nums[i]] >1:
                return True
        return False
        #return any(e > 1 for e in hashmap.values())