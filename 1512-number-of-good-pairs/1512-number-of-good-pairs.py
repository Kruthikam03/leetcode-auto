class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        
        count = 0
        for x in range(len(nums)):
            for y in range(x):
                if nums[x] == nums[y]:
                    count+=1

        return count