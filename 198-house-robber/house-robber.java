class Solution {
    public int rob(int[] nums) {
        int res=0;
        int nums_length=nums.length;
        ArrayList<Integer> dp = new ArrayList<>();
        if(nums_length==1){
            return nums[0];
        }
        if(nums_length==2){
            return Math.max(nums[0],nums[1]);
        }
        //we can use prev,curr to reduce spacial complexity
        dp.add(nums[0]);
        dp.add(Math.max(nums[0],nums[1]));
        for(int i=2;i<nums_length;i++){
            dp.add(Math.max(dp.get(i-1),nums[i]+dp.get(i-2)));
        }
        return dp.get(dp.size()-1);
        
    }
}