class Solution {
    public int climbStairs(int n) {
        ArrayList<Integer> array =new ArrayList<>();
        array.add(1);
        array.add(2);
        if(n==1){
            return array.get(0);
        }
        if(n==2){
            return array.get(1);
        }
        for(int i=2;i<n;i++){
            array.add(array.get(array.size()-1)+array.get(array.size()-2));
        }
        return array.get(array.size()-1);
    }
}