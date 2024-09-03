class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        text=s.strip().split()
        print(text)
        return len(text[-1])
        