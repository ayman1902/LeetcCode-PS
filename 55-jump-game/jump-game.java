class Solution {
    public boolean canJump(int[] nums) {
        int target=nums.length-1;
        for(int i=nums.length-1;i>-1;i--){
           if(i+nums[i]>=target){
                target=i;
           }
        }
        return target == 0;
        
    }
}