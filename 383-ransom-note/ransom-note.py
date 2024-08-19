class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazin_hashmap=defaultdict(int)
        for i in range(len(magazine)):
            magazin_hashmap[magazine[i]]+=1
        print(magazin_hashmap)
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazin_hashmap and magazin_hashmap[ransomNote[i]]>0:
                magazin_hashmap[ransomNote[i]]-=1
            else:
                return False
        return True
        print(magazin_hashmap)
        

        print(magazin_hashmap)
        