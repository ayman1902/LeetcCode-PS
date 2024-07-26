class Solution(object):
    def reverseVowels(self, s):
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        res=list(s)
        i=0 
        j=len(res)-1
        while i<j:
            if res[i] not in vowels:
                i+=1
                continue
            if res[j] not in vowels:
                j-=1
                continue
            res[i],res[j]=res[j],res[i]
            i+=1
            j-=1
        return "".join(res)
        