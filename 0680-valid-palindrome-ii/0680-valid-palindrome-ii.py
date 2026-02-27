class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)   # convert to list so we can remove

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                # Try removing left
                temp1 = s[left+1:right+1]
                
                # Try removing right
                temp2 = s[left:right]
                
                if temp1 == temp1[::-1] or temp2 == temp2[::-1]:
                    return True
                else:
                    return False
                break
            left += 1
            right -= 1
        else:
            return True