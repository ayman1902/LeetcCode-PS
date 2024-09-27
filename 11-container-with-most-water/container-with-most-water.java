class Solution {
    public int maxArea(int[] height) {
        int i=0;
        int j=height.length-1;
        int res=0;
        int res_m=0;
        while(i<j){
            res_m=(j-i)*(Math.min(height[i],height[j]));
            if(res_m>res){
                res=res_m;
            }
            if(height[j]<height[i]){
                j-=1;
            }
            else{
                i+=1;
            }

        }
        return res;
    }
}