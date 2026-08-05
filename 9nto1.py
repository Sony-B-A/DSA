# GFG
'''
Print n to 1 without loop
Difficulty: Easy
Print numbers from n to 1 (space separated) without the help of loops.
'''

class Solution:
    def printNos(self, n):
        # Code here
        if n ==0:
            return
        print(n, end=' ')
        self.printNos(n-1)