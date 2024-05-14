class Solution(object):
    def singleNonDuplicate(self, nums):
        low = 0
        high = len(nums)-1
        mid = low + (high-low)//2
        while low <= high:
            if len(nums) <= 1:
                return nums[0]
            if low < high and nums[low] == nums[low+1]:
                low += 2
            else:
                uniqueElement=nums[low]
                print(uniqueElement)
                low += 1
        return uniqueElement
        



        
        