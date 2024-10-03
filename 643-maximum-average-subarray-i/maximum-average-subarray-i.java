class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int nums_length=nums.length;
        double max_avg;
        int current_max=0;
        for(int i=0;i<k;i++){
            current_max+=nums[i];
        }
        max_avg= (double) current_max/k;
        for(int j=k;j<nums_length;j++){
            current_max+=nums[j];
            current_max-=nums[j-k];
            max_avg=Math.max(max_avg,(double) current_max/k);
        }
        return max_avg;
    }
}