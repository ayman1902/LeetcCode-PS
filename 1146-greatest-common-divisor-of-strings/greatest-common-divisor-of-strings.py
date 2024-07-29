class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1+str2 != str2+str1:
            return ""
        a=len(str1)
        b=len(str2)
        while b!=0:
            a,b=b,a%b
        print(a)
        return str1[:a]
        

        