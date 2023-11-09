class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        @lru_cache(None)
        def dp(i,holding=False,remain=2):

            if(i>=len(prices)):
                return 0

            option1,option2,option3 = 0,0,0
            # buying a new one
            if(not holding and remain>0):
                option1=-prices[i]+dp(i+1,True,remain-1)

            # selling owned
            if(holding):
                option2 = prices[i]+dp(i+1,False,remain)

            # do nothing
            option3 = dp(i+1,holding,remain)


            return max(option1,option2,option3)

        return dp(0)
        