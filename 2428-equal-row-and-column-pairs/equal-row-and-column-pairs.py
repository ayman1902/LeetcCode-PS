class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res=0
        row_hashmap = defaultdict(int)
        col_hashmap = defaultdict(int)

        for i in range(len(grid)):
            row_hashmap[hash(tuple(grid[i]))]+=1
            
        for j in range(len(grid[0])):
            col_hashmap[hash(tuple([grid[i][j] for i in range(len(grid))]))]+=1
        for key,value in row_hashmap.items():
            if key in col_hashmap:
                res+=value*col_hashmap[key]
        return res