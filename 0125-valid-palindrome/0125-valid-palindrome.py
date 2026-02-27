class Solution:
    def isPalindrome(self, s: str) -> bool:
        #s = "A man, a plan, a canal: Panama"

        clean = ""

        for ch in s:
            if ch.isalnum():
                clean += ch.lower()

        if clean == clean[::-1]:
            return True
        else:
            return False