class Solution(object):
    def minSubArrayLen(self, target, nums):
        n=len(nums)
        right=left=0
        minL=float('inf')
        sum=0
        length=0
        for right in range(n):
           sum+=nums[right]
           while sum >=target:
              length=right-left+1
              if length < minL:
                 minL=length
              sum-=nums[left]
              left+=1
        if minL != float('inf'): 
            return minL
        else:
            return 0
