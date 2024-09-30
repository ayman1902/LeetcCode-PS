class Solution {
    public void sortColors(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();

        for(int i=0;i<nums.length;i++){
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
        }
        final int[] start={0}; // foreach need a final variable so we use array as a wrapper
        map.forEach((key,value)->{
            System.out.println(key+";"+value);
            for(int a=start[0];a<start[0]+value;a++){
                nums[a]=key;
            }
            start[0]+=value;
        });
        System.out.print(Arrays.toString(nums));
        
    }
}