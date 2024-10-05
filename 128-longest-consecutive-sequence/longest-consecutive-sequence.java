class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        int longest=0;
        for(int num:nums){
            set.add(num);
        }
        for(int num:set){
            if(!set.contains(num-1)){
                int length=1;
                int next_num=num+1;
                while(set.contains(next_num)){
                    length+=1;
                    next_num+=1;
                }
                longest=Math.max(longest,length);
                System.out.println(num);
            }
        }
        System.out.println(set.toString());
        return longest;
        
    }
}