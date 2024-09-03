class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        text=s.split()
        print(text)
        return len(text[-1])
        