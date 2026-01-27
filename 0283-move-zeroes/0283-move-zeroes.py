class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        remove= 0

        for i in nums:
            if remove in nums:
                nums.remove(remove)
                nums.append(remove)
