class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        print(favoriteCompanies)
        hash_list= [set(hash(companie) for companie in companies) for companies in favoriteCompanies]
        print(hash_list)
        res=[]
        for i in range(len(hash_list)):
            is_subset=False
            for j in range(len(hash_list)):
                if j!=i and hash_list[i].issubset(hash_list[j]):
                    is_subset=True
                    break
            if is_subset == False:
                res.append(i)
        print(res)
        return res