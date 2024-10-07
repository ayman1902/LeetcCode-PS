class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        //b
        int res=0;
        HashMap<Character,Integer> mapStones=new HashMap<>();
        for(char c:stones.toCharArray()){
            mapStones.put(c,mapStones.getOrDefault(c,0)+1);
        }
        for(char jewel:jewels.toCharArray()){
            if(mapStones.containsKey(jewel)){
                res+=mapStones.get(jewel);
            }
        }
        return res;
    }
}