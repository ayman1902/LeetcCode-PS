class Solution {
    public int uniquePaths(int m, int n) {
        int res=0;
        int[][] matrixDp = new int[n][m];
        System.out.println(Arrays.deepToString(matrixDp));
        for(int j=0;j<m;j++){
            matrixDp[0][j]=1;
        }
        for(int i=0;i<n;i++){
            matrixDp[i][0]=1;
        }
        for(int i=1;i<n;i++){
            for(int j=1;j<m;j++){
                matrixDp[i][j]=matrixDp[i][j-1]+matrixDp[i-1][j];
            }
        }
        return matrixDp[n-1][m-1];
        
    }
}