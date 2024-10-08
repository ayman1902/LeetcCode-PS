class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(numbers)-1
        while i<j:
            res=numbers[i]+numbers[j]
            if res>target:
                j-=1
            elif res<target:
                i+=1
            else:
                return [i+1,j+1]
        