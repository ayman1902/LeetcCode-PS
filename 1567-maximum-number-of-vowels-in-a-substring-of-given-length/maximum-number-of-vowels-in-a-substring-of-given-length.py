class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        compara=0
        res=0
        for i in range(len(s)-k+1):
            for j in range(k):
                if s[i+j] in vowels:
                    compara +=1
            if compara > res:
                res=compara
            compara=0
        return res
        """
        res=0
        max_res=0
        vowels=set("aeiou")
        for i in range(k):
            if s[i] in vowels:
                res+=1
        max_res=res
        for i in range(k,len(s)):
            if s[i] in vowels:
                res+=1
            if s[i-k] in vowels:
                res-=1
            if res>max_res:
                max_res=res
            
        return max_res
        