class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: intg
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        def swaping(array,i,j):
            li=i
            rj=j
            while li<rj:#swwaping
                temp=array[li]
                array[li]=array[rj]
                array[rj]=temp

                li+=1
                rj-=1
        swaping(nums, 0, len(nums) - 1)
        swaping(nums, 0, k - 1)
        swaping(nums, k, len(nums) - 1)