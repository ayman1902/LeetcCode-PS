# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def binarysearch(start,fin):
            mid=(fin+start)//2
            g=guess(mid)
            if g== 0:
                return mid
            elif g ==1:
                return binarysearch(mid+1,fin)
            else:
                return binarysearch(start,mid-1)
        return binarysearch(0,n)
            
        