class Solution:
    def soupServings(self, n: int) -> float:

        if(n>4800):
            return 1
        
        @lru_cache(None)
        def dp(a,b):
            if(a<=0 and b<=0):
                return 0.5
            elif(a<=0):
                return 1
            elif(b<=0):
                return 0
            else:
                temp= 0.25*dp(a-100,b)
                temp+= 0.25*dp(a-75,b-25)
                temp+= 0.25*dp(a-50,b-50)
                temp+= 0.25*dp(a-25,b-75)

                return temp
        return dp(n,n)