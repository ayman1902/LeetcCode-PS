class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        int n=nums.length;
        Arrays.sort(nums);
        int hight=0;
        int low=0;
        for(int i=0;i<n;i++){
            if(nums[i]>0){
                break;
            }
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }
            low=i+1;
            hight=n-1;
            while(low<hight){
                int sum=nums[i]+nums[low]+nums[hight];
                if(sum==0){
                    List<Integer> sub_res=new ArrayList<>();
                    sub_res.add(nums[i]);
                    sub_res.add(nums[low]);
                    sub_res.add(nums[hight]);
                    res.add(sub_res);
                    low+=1;
                    hight-=1;
                    while(low<hight && nums[low]==nums[low-1]){
                        low+=1;
                    }
                    while(low<hight && nums[hight]==nums[hight+1]){
                        hight-=1;
                    }
                }
                else if(sum<0){
                    low+=1;
                }else{
                    hight-=1;
                }

            }
        }
        return res;
        
    }
}