class Solution {
    public void rotate(int[][] matrix) {
        //first the transposé
        int temp=0;
        System.out.println(Arrays.deepToString(matrix));
        for(int i=0;i<matrix.length;i++){
            for(int j=i;j<matrix[0].length;j++){
                temp=matrix[i][j];
                matrix[i][j]=matrix[j][i];
                matrix[j][i]=temp;
            }
        }
        //reverse each aray
        for(int k=0;k<matrix.length;k++){
            reverseArray(matrix[k]);

        }
        System.out.println(Arrays.deepToString(matrix));
    }
    public static void reverseArray(int[] array){
        int temp=0;
        int left=0;
        int right=array.length-1;
        while(left<right){
            temp=array[left];
            array[left]=array[right];
            array[right]=temp;
            left++;
            right--;
        }
    }
}