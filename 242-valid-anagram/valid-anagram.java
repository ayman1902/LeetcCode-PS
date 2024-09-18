class Solution {

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> hashmapS = new HashMap<Character, Integer>();
        HashMap<Character, Integer> hashmapT = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            hashmapS.put(s.charAt(i), hashmapS.getOrDefault(s.charAt(i), 0) + 1);
            hashmapT.put(t.charAt(i), hashmapT.getOrDefault(t.charAt(i), 0) + 1);
        }
        return hashmapS.equals(hashmapT);
    }
}
