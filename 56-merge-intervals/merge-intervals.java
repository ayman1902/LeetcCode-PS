class Solution {
    public int[][] merge(int[][] intervals) {
        ArrayList<int[]> merged =new ArrayList<>();
        System.out.println(Arrays.deepToString(intervals));
        Arrays.sort(intervals,Comparator.comparingInt(a->a[0]));
        System.out.println(Arrays.deepToString(intervals));
        for(int[] interval : intervals){
            if(merged.isEmpty() || merged.get(merged.size()-1)[1]<interval[0]){
                merged.add(interval);
            }else{
                int[] lastInterval = merged.get(merged.size()-1);
                merged.set(merged.size()-1,new int[]{lastInterval[0],Math.max(lastInterval[1],interval[1])});
            }
             System.out.println(Arrays.toString(interval));
        }

        return merged.toArray(new int[merged.size()][2]);
    }
}