class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        arr=[0,1]
        direction=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        res = [[0] * len(board[0]) for _ in range(len(board))]
        print(res)
        for i in range(len(board)):
            for j in range(len(board[0])):
                live_neighboard=0
                for di,dj in direction:
                    if 0<=di+i<len(board) and 0<=dj+j<len(board[0]) and board[di+i][dj+j]==1:
                        live_neighboard+=1
                
                print(i,j,live_neighboard)
                if board[i][j]==0 and live_neighboard==3:
                    res[i][j]=1
                elif board[i][j]==1 and live_neighboard <2:
                    res[i][j]=0
                elif board[i][j]==1 and 2<=live_neighboard <=3:
                    res[i][j]=1
                elif board[i][j]==1 and live_neighboard >3:
                    res[i][j]=0


        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]=res[i][j]
        return board