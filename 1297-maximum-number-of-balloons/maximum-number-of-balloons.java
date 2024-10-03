class Solution {
    public int maxNumberOfBalloons(String text) {
        HashMap<Character,Integer> map = new HashMap<>();
        int res=0;
        for(int i=0;i<text.length();i++){
            map.put(text.charAt(i),map.getOrDefault(text.charAt(i),0)+1);
        }
        System.out.println(map.toString()+map.getOrDefault('b',0));
        int countB=map.getOrDefault('b',0);
        int countA=map.getOrDefault('a',0);
        int countL=map.getOrDefault('l',0)/2;
        int countO=map.getOrDefault('o',0)/2;
        int countN=map.getOrDefault('n',0);
        return Math.min(Math.min(Math.min(Math.min(countB,countA),countL),countO),countN);
    }
}