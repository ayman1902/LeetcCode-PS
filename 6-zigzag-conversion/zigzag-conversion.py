class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n=len(s)
        if n==1:
            return s
        index=1
        track_matrix=[[s[i],0] for i in range(n)]
        going_down=False
        hashmap=defaultdict(str)
        for i in range(len(track_matrix)):
            track_matrix[i][1]=index
            hashmap[index]+=s[i]
            if going_down == False:
                index+=1
            if going_down==True:
                index-=1
            if index==numRows:
                going_down=True
            if index==1:
                going_down=False
        result = ''.join(hashmap[i] for i in hashmap)
        return result
        