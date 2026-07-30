# GeeksForGeeks
# Easy

"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        freq_map = {}
        
        for num in arr:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
                
        if x in freq_map:
            return freq_map[x]
        else:
            return 0