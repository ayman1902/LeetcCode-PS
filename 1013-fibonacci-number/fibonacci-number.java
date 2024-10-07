class Solution {
    public int fib(int n) {
        List<Integer> dp = new ArrayList<>();
        dp.add(0);
        dp.add(1);
        if(n==0){
            return 0;
        }
        if(n==1){
            return 1;
        }
        for(int i=2;i<=n;i++){
            dp.add(dp.get(i-1)+dp.get(i-2));
        }
        return dp.get(n);
        
    }
}