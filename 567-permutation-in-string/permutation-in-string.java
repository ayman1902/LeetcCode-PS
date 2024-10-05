class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] s1_count = new int[26];
        int[] s2_count = new int[26];
        int s1_length = s1.length();
        int s2_length = s2.length();
        if(s1_length>s2_length){
            return false;
        }
        for(int i=0;i<s1_length;i++){
            s1_count[s1.charAt(i) - 'a']++;
            s2_count[s2.charAt(i) - 'a']++;
        }
        if(Arrays.equals(s1_count,s2_count)){
            return true;
        }
        for(int i=s1_length;i<s2_length;i++){
            s2_count[s2.charAt(i) - 'a']++;
            s2_count[s2.charAt(i-s1_length) - 'a']--;
            if(Arrays.equals(s1_count,s2_count)){
                 return true;
            }
        }
        return false;
        
    }
}