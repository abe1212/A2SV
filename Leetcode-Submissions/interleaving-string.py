class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        s1_len = len(s1)
        s2_len = len(s2)

        @lru_cache(None)
        def dp(i,j):

            if(i==s1_len and j==s2_len):
                return True

            answers = []
            if(i<s1_len and s1[i]==s3[i+j]):
                answers.append(dp(i+1,j))
            
            if(j<s2_len and s2[j]==s3[i+j]):
                answers.append(dp(i,j+1))
            
            return any(answers)
        
        if len(s1) +len(s2) != len(s3):
            return False

        return dp(0,0)
        