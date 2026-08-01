'''
GeeksForGeeks
1 to n Without Loops
Difficulty: Basic

Given an positive integer n, print numbers from 1 to n without using loops.
Implement the function printTillN() to print the numbers from 1 to n as space-separated integers.
'''
class Solution:
    def printTillN(self, n):
    	#code here 
    	if n == 0:
    	    return
    	self.printTillN(n-1)
    	print(n, end=' ')