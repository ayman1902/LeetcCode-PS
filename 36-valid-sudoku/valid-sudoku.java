class Solution {
    public boolean isValidSudoku(char[][] board) {
        //check rows
        for(int i=0;i<9;i++){
            HashSet<Integer> set = new HashSet<>();
            for(int j=0;j<9;j++){
                char item= board[i][j];
                if(set.contains((int) item)){
                    return false;
                }
                if(item!='.'){
                    set.add((int) item);
                }
            }
        }
        //check columns
         for(int i=0;i<9;i++){
            HashSet<Integer> set = new HashSet<>();
            for(int j=0;j<9;j++){
                char item= board[j][i];
                if(set.contains((int) item)){
                    return false;
                }
                if(item!='.'){
                    set.add((int) item);
                }
            }
        }
        //check boxes
        int[][] starts ={{0,0},{0,3},{0,6},
                         {3,0},{3,3},{3,6},
                         {6,0},{6,3},{6,6}};

        for(int[] box : starts){
            int a=box[0];
            int b=box[1];
            HashSet<Integer> set = new HashSet<>();
            for(int i=a;i<a+3;i++){
                for(int j=b;j<b+3;j++){
                    char item= board[i][j];
                    if(set.contains((int) item)){
                        return false;
                    }
                    if(item!='.'){
                        set.add((int) item);
                    }
                }
        }
        }
        return true;
    }
}