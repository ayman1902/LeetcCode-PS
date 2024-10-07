class Solution {
    public int[] sortedSquares(int[] nums) {
        int n=nums.length;
        int[] res = new int[n];
        int pointer=n-1;
        int left=0;
        int right=n-1;
        while(left<=right){
            if(Math.abs(nums[right])>Math.abs(nums[left])){
                res[pointer]=(int) Math.pow(nums[right],2);
                right--;
                pointer--;
            }else{
                res[pointer]=(int) Math.pow(nums[left],2);
                left++;
                pointer--;
            }
            
        }
        return res;
    }
}