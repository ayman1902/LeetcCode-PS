class Solution {
    public boolean canJump(int[] nums) {
        int numsLength=nums.length;
        int target=numsLength-1;
        for(int i=numsLength-1;i>-1;i--){
           if(i+nums[i]>=target){
                target=i;
           }
        }
        return target == 0;
        
    }
}