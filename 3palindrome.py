# Leetcode

# 9. Palindrome Number
# Easy
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = x
        rev = 0

        while n > 0:
            rev = (rev * 10) + (n % 10)
            n = n // 10

        if rev == x:
            return True
        return False