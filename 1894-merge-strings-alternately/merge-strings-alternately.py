class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l1=len(word1)
        l2=len(word2)
        bigg_word = word1 if len(word1) > len(word2) else word2
        res=""
        for i in range(min(l1,l2)):
            res+=word1[i]+word2[i]
        return res+bigg_word[min(l1,l2):]
