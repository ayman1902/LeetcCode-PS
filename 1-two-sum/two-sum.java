class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map=new HashMap<Integer,Integer>();
        int comb=0;
        for(int i=0;i<nums.length;i++){
            comb=target-nums[i];
            if(map.containsKey(comb)){
                return new int[]{map.get(comb),i};
            }
            map.put(nums[i],i);
        }
        return new int[]{,};

    }
}