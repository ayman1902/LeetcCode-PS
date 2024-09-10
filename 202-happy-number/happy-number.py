class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen=set()
        def nextHappyNumber(n):
            return sum([int(digits)**2 for digits in str(n)])
        
        while n not in seen and n!=1:
            seen.add(n)
            n=nextHappyNumber(n)
        return n==1
        