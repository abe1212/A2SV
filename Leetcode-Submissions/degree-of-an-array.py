class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        first_occurrence = {}
        last_occurrence = {}
        frequency = {}

        # Populate dictionaries
        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            last_occurrence[num] = i
            frequency[num] = frequency.get(num, 0) + 1

        # Calculate the degree of the array
        max_frequency = max(frequency.values())

        # Find the minimum length of subarrays with the same degree
        min_length = float('inf')
        for num, freq in frequency.items():
            if freq == max_frequency:
                min_length = min(min_length, last_occurrence[num] - first_occurrence[num] + 1)

        return min_length

