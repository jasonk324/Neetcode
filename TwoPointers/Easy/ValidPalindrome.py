class Solution(object):
    def isPalindrome(self, s):
        clean_str = ""

        for char in s:
            if char.isalnum():
                clean_str += char.lower()

        if clean_str == clean_str[::-1]:
            return True
        else: 
            return False