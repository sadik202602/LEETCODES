import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        subject = re.sub('[^a-zA-Z0-9]', '', s).lower()
        
        if subject == subject[::-1]:
            return True
        else:
            return False