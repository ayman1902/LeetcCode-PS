class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        hashmap_ligne=defaultdict(int)
        hashmap_cologne=defaultdict(int)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    hashmap_ligne[i]+=1
                    hashmap_cologne[j]+=1
        print(hashmap_ligne)
        print(hashmap_cologne)
        for key,value in hashmap_ligne.items():
            matrix[key]=[0 for i in range(len(matrix[0]))]
        for key,value in hashmap_cologne.items():
            for i in range(len(matrix)):
                matrix[i][key]=0
        return matrix
        