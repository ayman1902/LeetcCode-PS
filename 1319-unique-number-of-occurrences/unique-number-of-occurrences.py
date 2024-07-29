class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hashmap={}
        for i in range(len(arr)):
            if arr[i] in hashmap:
                hashmap[arr[i]]+=1
            else:
                hashmap[arr[i]]=1
        for index, key in enumerate(hashmap):
            if index ==0:
                res=[hashmap[key]]
            else:
                if hashmap[key] in res:
                    return False
                res.append(hashmap[key])
        return True