class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        hashmap_s=defaultdict(int)
        hashmap_t=defaultdict(int)
        for i in range(len(s)):
            hashmap_s[s[i]]+=1
            hashmap_t[t[i]]+=1
        return hashmap_s==hashmap_t