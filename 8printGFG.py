# GeeksForGeeks
'''
Print GFG n times
Difficulty: Easy
Given a positive number n, print the string "GFG" exactly n times separated by a single space.
'''
n = int(input())

# Code here
def printGFG(n):
    if n == 0:
        return
    print('GFG', end=' ')
    printGFG(n-1)
    
printGFG(n)