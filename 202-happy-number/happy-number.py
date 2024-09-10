class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seeen=set()
        def nextHappyNumber(n):
            return sum([int(digits)**2 for digits in str(n)])
        
        while n not in seeen and n!=1:
            seeen.add(n)
            n=nextHappyNumber(n)
        return n==1
        