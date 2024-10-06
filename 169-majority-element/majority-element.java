class Solution {
    public int majorityElement(int[] nums) {
        int lim=(int) nums.length/2;
        HashMap<Integer,Integer> map =new HashMap<>();
        for(int num:nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        for(Integer key:map.keySet()){
            if(map.get(key)>lim){
                return key;
            }
        }
        return -1;
    }
}