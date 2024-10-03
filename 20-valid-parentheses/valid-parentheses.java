class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character,Character> map=new HashMap<>();
        map.put('{','}');
        map.put('(',')');
        map.put('[',']');

        for(int i=0;i<s.length();i++){
            char currentChar=s.charAt(i);
            if(map.containsKey(s.charAt(i))){
                stack.push(currentChar);
            }else{
                if(stack.isEmpty() || map.get(stack.peek())!=currentChar){
                    return false;
                }
                stack.pop();
            }
        }
        return stack.isEmpty();
    }
}