class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def bit(number):
            res=0
            while number>0:
                res+=number%2
                number=number//2
            return res

        res=[0]*(n+1)
        for i in range(n+1):
            res[i]=bit(i)
        # res[i]=res[i>>1] + i%2

        return res