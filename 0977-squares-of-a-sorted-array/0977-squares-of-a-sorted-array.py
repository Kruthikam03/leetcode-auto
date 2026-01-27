class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square=0
        result=[]

        for i in nums:
            square=i*i
            result.append(square)
            result.sort()
        return result