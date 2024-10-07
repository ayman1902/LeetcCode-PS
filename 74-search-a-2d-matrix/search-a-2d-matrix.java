class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int n=matrix.length;
        int m=matrix[0].length;
        int low=0;
        int hight=m*n-1;
        while(low<=hight){
            int mid=(hight+low)/2;
            if(matrix[mid/m][mid%m]==target){
                return true;
            }
            else if(matrix[mid/m][mid%m]<target){
                low=mid+1;
            }else{
                hight=mid-1;
            }
        }
        return false;
    }
}