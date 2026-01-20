class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = 0
        res=[0]
        for i in gain:
            n+=i
            res.append(n)
        return max(res)