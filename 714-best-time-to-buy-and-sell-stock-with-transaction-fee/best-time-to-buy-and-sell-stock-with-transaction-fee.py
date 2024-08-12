class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n=len(prices)
        if n==0:
            return 0
        dp=[[0]*2 for i in range(n)]
        #hold
        dp[0][0]=-prices[0]
        #cach
        dp[0][1]=0
        
        for i in range(1,n):
            #hold so hold or bi3e
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i]-fee)
            #cach so rta7 wla chri
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i])
        return dp[n-1][1]
        