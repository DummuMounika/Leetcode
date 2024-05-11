class Solution(object):
    def productExceptSelf(self, nums):
        left=[0]*len(nums) 
        right=[0]*len(nums) 
        left[0]=1 
        for i in range(1,len(nums)): #[1,1,2,6]
            left[i]=left[i-1]*nums[i-1] 
        right[len(nums)-1]=1 
        for i in range(len(nums)-2,-1,-1): #[24,12,4,1]
            right[i]=right[i+1]*nums[i+1] 
        res=[0]*len(nums) 
        for i in range(len(nums)): #[24,12,8,6]
            res[i]=left[i]*right[i]
        return res
        
        