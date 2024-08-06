class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        hashmap={#mappage
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res=[]
        if digits=="":
            return []
        def backtracking(combinaision,index):
            if not index:#to the last digits
                res.append(combinaision)
            else:
                for letter in hashmap[index[0]]:
                    backtracking(combinaision + letter,index[1:])#mixing
        backtracking("",digits)
        return res
