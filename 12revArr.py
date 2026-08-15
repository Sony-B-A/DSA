# GFG
'''
Reverse Subarray
Difficulty: Basic
Given an array arr, you need to reverse a subarray of that array. The range of this
subarray is given by indices l and r (1-based indexing).

Examples:

Input: arr[] = [1, 2, 3, 4, 5, 6, 7], l = 2, r = 4
Output: [1, 4, 3, 2, 5, 6, 7]
Explanation: After reversing the elements in range 2 to 4 (2, 3, 4),
modified array is 1, 4, 3, 2, 5, 6, 7.
'''

# Method 1 - using 2 functions

class Solution:
    def rev(self, arr, l, r):
        if l >= r:
            return
        arr[l], arr[r] = arr[r], arr[l]
        return self.rev(arr, l + 1, r - 1)
    
    def reverseSubArray(self,arr,l,r):
        # code here
        l = l - 1
        r = r - 1
        self.rev(arr, l, r)
        return arr

# Method 2 - using while loop

class Solution:
    def reverseSubArray(self,arr,l,r):
        # code here
        l-=1
        r-=1
        while l<r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l+1, r-1
        return arr


# method 3 - using nested functions

class Solution:
    def reverseSubArray(self,arr,l,r):
        # code here
        l = l - 1
        r = r - 1
        
        def rev(arr, l, r):
            if l >= r:
                return arr
                
            arr[l], arr[r] = arr[r], arr[l]
            return rev(arr, l + 1, r - 1)
        
        rev(arr, l, r)
            
        return arr