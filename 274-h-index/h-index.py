class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        n=len(citations)
        h=0
        for i in range(n):
            if citations[i]>=i+1:
                h+=1
            else:
                break
        return h