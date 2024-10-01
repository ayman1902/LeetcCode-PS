class Solution {
    public int search(int[] nums, int target) {
        int start=0;
        int end=nums.length;
        int med=0;
        System.out.println(start+" "+end+" "+target);
        while(start<end){
            med=(start+end)/2;
            System.out.println(med+" "+nums[med]);
            if(nums[med]==target){
                return med;
            }
            if(nums[med]<target){
                start=med+1;
            }
            else{
                end=med;
            }
        }
        return -1;
    }
}