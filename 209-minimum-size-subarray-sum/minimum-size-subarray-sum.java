class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int start=0;
        int end=0;
        int count=nums[0];
        double min_lenght=Double.POSITIVE_INFINITY;
        while (end<nums.length){
            if(count<target){
                end++;
                if(end<nums.length){
                    count+=nums[end];
                }
            }
            else{
                min_lenght=Math.min(min_lenght,end-start+1);
                count-=nums[start];
                start++;
            }
        }
        if(Double.isInfinite(min_lenght)==true){
            return 0;
        }
        return (int) Math.round(min_lenght);
    }
}