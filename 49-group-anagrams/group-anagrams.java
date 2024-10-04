class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        HashMap<String,List<String>> anagram_map = new HashMap<>();
        

        for(String str:strs){
            int[] temp = new int[26];
            for(char c:str.toCharArray()){
                temp[c - 'a']+=1;
            }
            String key=Arrays.toString(temp);
            //anagram_map.put(temp,str);
            anagram_map.putIfAbsent(key, new ArrayList<>());
            anagram_map.get(key).add(str);
        }
        anagram_map.forEach((key,value)->{
            res.add(value);
        });

        System.out.println(res.toString());
        System.out.println(anagram_map.toString());
        
        return res;

    }
}