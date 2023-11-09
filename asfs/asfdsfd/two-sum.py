class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dic={}

        for i in range(len(nums)):
            if( (target-nums[i]) in diff_dic ):
                return [diff_dic[target-nums[i]],i]

            else:
                diff_dic[nums[i]]=i