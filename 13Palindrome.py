# GFG
'''
Palindrome String
Difficulty: Easy
Given a string s, return true if the string is a palindrome. Otherwise, return false.
A string is considered a palindrome if it reads the same forwards and backwards.
'''

class Solution:
    def isPalindrome(self, s):
        # code here
        s = s.lower()
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
