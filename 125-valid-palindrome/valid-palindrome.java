class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder phraseAfterModif =new StringBuilder();
        
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                phraseAfterModif.append(Character.toLowerCase(c));
            }
        }
        int low=0;
        int hight=phraseAfterModif.length() - 1;
        System.out.println(phraseAfterModif.toString()+" "+low+" "+hight);

        while(low<hight){
            if(phraseAfterModif.charAt(low)!=phraseAfterModif.charAt(hight)){
                return false;
            }
            low++;
            hight--;
        }
        
        System.out.println(phraseAfterModif.toString()+" "+low+" "+hight);
        return true;
    }
}