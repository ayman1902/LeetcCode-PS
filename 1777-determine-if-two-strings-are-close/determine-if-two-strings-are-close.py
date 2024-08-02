class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1)!=len(word2):
            return False
        d1=defaultdict(int)
        d2=defaultdict(int)
        for i in range(len(word1)):
            d1[word1[i]] +=1
            d2[word2[i]] +=1
        if set(d1)!=set(d2):
            return False
        if sorted(d1.values()) != sorted(d2.values()):
            return False
        return True
        