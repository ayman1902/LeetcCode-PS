class Solution {
    public int calPoints(String[] operations) {
        int res=0;
        Stack<Integer> stack =new Stack<>();
        for(String op:operations){
            if(op.equals("+")){
                int a=stack.pop();
                int b=stack.peek();
                int c=a+b;
                stack.push(a);
                stack.push(c);
            }
            else if(op.equals("D")){
                stack.push(2*stack.peek());
            }
            else if(op.equals("C")){
                stack.pop();
            }
            else{
                System.out.println(op);
                stack.push(Integer.parseInt(op));
            }
        }
        while(!stack.isEmpty()){
            res+=stack.pop();
        }
        return res;
    }
}