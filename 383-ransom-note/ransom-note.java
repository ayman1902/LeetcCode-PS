class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character,Integer> magazinMap = new HashMap<>();
        for(int i=0;i<magazine.length();i++){
            char item=magazine.charAt(i);
            magazinMap.put(item,magazinMap.getOrDefault(item,0)+1);
        }
        for(int i=0;i<ransomNote.length();i++){
            char item=ransomNote.charAt(i);
            if(magazinMap.containsKey(item) && magazinMap.get(item)>0){
                magazinMap.put(item,magazinMap.getOrDefault(item,0)-1);
            }else{
                return false;
            }
        }
        return true;
    }
}