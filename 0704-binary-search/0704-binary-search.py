class Solution(object):
    def recursiveSearch(self, nums, low, high, target):
        if low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return self.recursiveSearch(nums,mid+1,high,target)
            else: 
                return self.recursiveSearch(nums,low,mid-1,target) 
        return -1

    def search(self, nums, target):
        return self.recursiveSearch(nums,0,len(nums)-1,target)
        
                
        
        