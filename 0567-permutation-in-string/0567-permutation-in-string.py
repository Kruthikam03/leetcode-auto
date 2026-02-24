class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        for i in range(len(s2) - k + 1):
            window = s2[i:i+k]
            #print(window)
            if sorted(s1)==sorted(window):
                return True
            
        return False