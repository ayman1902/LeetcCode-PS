class Solution {
    public int maxSubArray(int[] nums) {
        List<Integer> subbArray =new ArrayList<>();
        subbArray.add(nums[0]);
        int currentSum=nums[0];
        int maxSum=nums[0];
        for(int i=1;i<nums.length;i++){
            if(currentSum+nums[i]>nums[i]){
                subbArray.add(nums[i]);
                currentSum+=nums[i];
            }else{
                subbArray.clear();
                subbArray.add(nums[i]);
                currentSum=nums[i];
            }
            maxSum=Math.max(maxSum,currentSum);
        }
        return maxSum;
        
    }
}