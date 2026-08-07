# GFG

'''Factorial
Difficulty: Basic
Given a positive integer, n. Find the factorial of n.
'''
class Solution:
    def factorial(self, n: int) -> int:
        # code here
        if n== 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)