class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        hashmap={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        for i in range(len(s)-1,-1,-1):
            current_value=hashmap[s[i]]
            if i+1<len(s) and current_value<hashmap[s[i+1]]:
                res-=current_value
            else:
                res+=current_value
        return res