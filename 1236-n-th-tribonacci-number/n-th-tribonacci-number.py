class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        res=[0,1,1]
        for i in range(2,n):
            res.append(res[i]+res[i-1]+res[i-2])
        return res[-1]