class Solution {
    public int minCostClimbingStairs(int[] cost) {
        ArrayList<Integer> dp =new ArrayList<>();
        dp.add(0);
        dp.add(0);

        for(int i=2;i<cost.length+1;i++){
            dp.add(Math.min(dp.get(i-1)+cost[i-1],dp.get(i-2)+cost[i-2]));
        }
        return dp.get(dp.size()-1);
    }
}