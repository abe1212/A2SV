class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        stack = []
        max_2 = float('-inf')

        for i in range(n - 1, -1, -1):
            if nums[i] < max_2:
                return True
            while stack and nums[i] > stack[-1]:
                max_2 = stack.pop()
            stack.append(nums[i])

        return False