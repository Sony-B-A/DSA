# GFG
'''
Sum of Natural Number Cubes
Difficulty: Basic
Given an integer n, calculate the sum of series 1^3 + 2^3 + 3^3 + 4^3 + … till n-th term.
'''
class Solution:
    def sumOfSeries(self,n):
        #code here
        if n == 0:
            return 0
        return n ** 3 + self.sumOfSeries(n - 1)
        