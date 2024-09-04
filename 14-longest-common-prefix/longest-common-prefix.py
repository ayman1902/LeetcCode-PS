class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        res=0
        hashmap=defaultdict(int)
        min_lenght=min([len(strings) for strings in strs])
        for i in range(min_lenght):
            for strings in strs:
                hashmap[strings[i]]+=1
            if len(hashmap) ==1:
                res+=1
            else:
                break
            hashmap.clear()
        if res==0:
            return ""
        return strs[0][:res]
        