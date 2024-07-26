class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        hashmap1={}
        hashmap2={}

        for i in range(len(nums1)):
            if nums1[i] in hashmap1:
                hashmap1[nums1[i]] +=1
            hashmap1[nums1[i]]=1
        for j in range(len(nums2)):
            if nums2[j] in hashmap2:
                hashmap2[nums2[j]] +=1
            hashmap2[nums2[j]]=1
        unique1=[num for num in hashmap1 if num not in hashmap2]
        unique2=[num for num in hashmap2 if num not in hashmap1]
        return [unique1,unique2]
        