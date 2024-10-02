class Solution {
    public String longestCommonPrefix(String[] strs) {
        int minum_length=strs[0].length();
        int minimum_prefix_length=0;
        int k=0;
        //nadiiiiiiiiii
        if (strs == null || strs.length == 0) {
            return "";
        }
        for(int i=1;i<strs.length;i++){
            if(strs[i].length()<minum_length){
                minum_length=strs[i].length();
            }
        }
        while(k<minum_length){
            for(int j=0;j<strs.length;j++){
                if(strs[j].charAt(k)!=strs[0].charAt(k)){
                    return strs[0].substring(0,k);
                }
            }
            k++;  
        }
        return strs[0].substring(0, minum_length);
    }
    
}