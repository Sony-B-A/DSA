'''
GeeksForGeeks

Number of factors
Difficulty: Easy
Find the number of factors for a given integer n.
'''
class Solution:
    def countFactors (self, n):
        from math import sqrt
        # code here
        num = n
        count = 0
        from math import sqrt
        
        for i in range(1, int(sqrt(num)) + 1):
            if(num % i == 0):
                count += 1
                if(num // i != i):
                    count += 1
                    
        return count