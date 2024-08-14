class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res=[]
        hashmap=defaultdict(int)
        for i in range(len(strs)):
            anares=''.join(sorted(strs[i]))
            if anares not in hashmap:
                hashmap[anares]=[]
            hashmap[anares].append(strs[i])
        return hashmap.values()
        #for key,value in hashmap.items():
        #    res.append([strs[val] for val in value])
        #eturn res