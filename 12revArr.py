# GFG

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

arr = [1, 2, 3, 4, 5]
o = Solution()
print(o.reverseSubArray(arr, 1, len(arr)))