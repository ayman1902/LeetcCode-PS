class Solution {
    public boolean isSubsequence(String s, String t) {
        int j=0;
        int s_length=s.length();
        for(int i=0;i<t.length();i++){
            System.out.println(t.charAt(i)+" "+j);
            if(j<s_length  &&  t.charAt(i)==s.charAt(j)){
                j++;
            }
        }
        if(j==s_length){
            return true;
        }
        return false;
    }
}