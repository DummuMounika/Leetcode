class Solution(object):
    def searchInsert(self, nums, target):

        low = 0
        high = len(nums)-1 
        while low <= high:
            mid = low + (high-low)//2

            #check if target is present at mid
            if nums[mid] == target:
                return mid

            # If target is greater, ignore left half
            elif target > nums[mid]:
                low = mid + 1

            # If target is smaller, ignore right half
            else:
                high = mid - 1
        # If element is not present, return the insertion point  
        return low
                