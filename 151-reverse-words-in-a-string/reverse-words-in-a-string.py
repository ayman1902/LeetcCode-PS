class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        res=""
        for i in range(len(words)-1,-1,-1):
            res+= words[i]
            if i!=0:
                res+=" "
        return res


        