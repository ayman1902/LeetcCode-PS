class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap=defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in hashmap and int(i-hashmap[nums[i]])<=k:
                return True
            else:
                hashmap[nums[i]]=i
        return False