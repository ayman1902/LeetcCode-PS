from collections import defaultdict
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        res = ""
        max_count= 0
        paragraph = paragraph.lower()
        counter_map = defaultdict(int)
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch," ")
        words = paragraph.split()
        for word in words:
            if word not in banned:
                counter_map[word]+=1
        return max(counter_map , key = counter_map.get)
