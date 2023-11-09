class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        previous = 0
        for num in arr:
            prev_k=k
            if((num-previous)>1):
                k-=(num-previous)-1
            if(k<=0):
                return previous+prev_k
            previous=num

        return previous+k
        