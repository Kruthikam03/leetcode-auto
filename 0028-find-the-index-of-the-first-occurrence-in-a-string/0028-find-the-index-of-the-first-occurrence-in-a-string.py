class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=len(needle)

        for i in range(len(haystack)-k+1):
            window=haystack[i:i+k]
            
            if needle==window:
                
                return i
                break
            
        return -1