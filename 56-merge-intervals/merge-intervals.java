class Solution {
    public int[][] merge(int[][] intervals) {
        ArrayList<int[]> merged =new ArrayList<>();
        Arrays.sort(intervals,Comparator.comparingInt(a->a[0]));
        for(int[] interval : intervals){
            if(merged.isEmpty() || merged.get(merged.size()-1)[1]<interval[0]){
                merged.add(interval);
            }else{
                int[] lastInterval = merged.get(merged.size()-1);
                merged.set(merged.size()-1,new int[]{lastInterval[0],Math.max(lastInterval[1],interval[1])});
            }
        }

        return merged.toArray(new int[merged.size()][2]);
    }
}