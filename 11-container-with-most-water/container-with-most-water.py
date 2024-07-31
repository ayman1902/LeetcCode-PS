class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        res_f=0
        while i<j:
            res=(j-i)*min(height[i],height[j])
            if res>res_f:
                res_f=res
            if height[j]<height[i]:
                j-=1
            else:
                i+=1
        return res_f
        