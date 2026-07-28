# 7. Reverse Integer
# Level: Medium

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go
# outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        import math
        n = abs(x)
        res = 0

        while n > 0:
            res = (res * 10) + (n % 10)
            n = n // 10
            
        if x < 0:
            res = -(res)

        if(res < -2**31 or res > (2 ** 31)-1):
            return 0
        else:
            return res
