class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n=len(matrix[0])
        m=len(matrix)
        left,right=0,n*m-1
        while left<=right:
            mid=(left+right)//2
            mid_value=matrix[mid//n][mid%n]
            if mid_value==target:
                return True
            elif mid_value>target:
                right=mid-1
            else:
                left=mid+1
        return False
        