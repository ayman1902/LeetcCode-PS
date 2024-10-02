class Solution {
    public int findClosestNumber(int[] nums) {
        int res=nums[0];
        for(int i=1;i<nums.length;i++){
            if(Math.abs(nums[i])<Math.abs(res)){
                res=nums[i];
            }
        }
        if(res<0 && numberInArray(Math.abs(res),nums)){
            res=-res;
        }
        System.out.println(res);
        return res;
    }
    public static boolean  numberInArray(int number,int[] array){
        for(int k=0;k<array.length;k++){
            if(array[k]==number){
                return true;
            }
        }
        return false;
    }
}