class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder merged=new StringBuilder();
        String bigWord=new String();
        int length_1=word1.length();
        int length_2=word2.length();
        int min_length=Math.min(length_1,length_2);
        if(length_1>length_2){
            bigWord=word1;
        }else{
            bigWord=word2;
        }
        for(int i=0;i<min_length;i++){
            merged.append(word1.charAt(i)).append(word2.charAt(i));
        }
        for(int j=min_length;j<bigWord.length();j++){
            merged.append(bigWord.charAt(j));
        }
        return merged.toString();
        
    }
}