class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        int res=0;
        String operateurs="+-/*";
        for(String token : tokens){
            if(operateurs.contains(token)){
                int b = stack.pop();
                int a = stack.pop();
                if(token.equals("+")){
                    stack.push(a+b);
                }
                if(token.equals("-")){
                    stack.push(a-b);
                }
                if(token.equals("/")){
                    stack.push(a/b);
                }
                if(token.equals("*")){
                    stack.push(a*b);
                }
            }
            else{
              stack.push(Integer.parseInt(token));  
            }
            
        }

        System.out.println(stack.toString());
        return stack.pop();
    }
}