class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        print(strs)
        res=0
        hashmap=defaultdict(int)
        print(hashmap)
        min_lenght=min([len(strings) for strings in strs])
        print(min_lenght)
        for i in range(min_lenght):
            for strings in strs:
                hashmap[strings[i]]+=1
            print(hashmap,len(hashmap))
            if len(hashmap) ==1:
                res+=1
            else:
                break
            hashmap.clear()
        print(res)
        if res==0:
            return ""
        return strs[0][:res]
        