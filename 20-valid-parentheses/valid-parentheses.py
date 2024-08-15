class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        hashmap={"(":")","{":"}","[":"]"}
        for i in range(len(s)):
            if s[i] in hashmap:
                stack.append(s[i]) 
            else:
                if not stack or s[i]!=hashmap[stack[-1]]:
                    return False
                stack.pop()
            
        return not stack
        