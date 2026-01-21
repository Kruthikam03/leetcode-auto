class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        min_value=min(nums)
        max_value=max(nums)

        for i in range(0,max_value+2):
            if i not in nums:
                return i